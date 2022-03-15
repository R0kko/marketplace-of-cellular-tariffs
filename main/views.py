from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from main.forms import RegistrationForm, LoginForm, FullPersonalInformationForm, ChangePasswordForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import check_password

from main.models import SupplementedUser, Notification, Tariff, Operator, Favorite_fact
from marketplace_of_ct.settings import MAX_GB, MAX_MINUTES, MIN_MINUTES, MIN_GB, MAX_PRICE, MIN_PRICE, MIN_MESSAGES, MAX_MESSAGES
from random import randint


# Create your views here.

def get_base_context(request, pagename: str = "Page"):
    user = SupplementedUser.objects.filter(user_id=request.user.id).first()
    if user:
        user.new_notifications_count = len(Notification.objects.filter(receiver=user))
        user.save()
    return {
        'is_authenticated': request.user.is_authenticated,
        'pagename': pagename,
        'User': get_object_or_404(SupplementedUser, user_id=request.user.id) if request.user.is_authenticated else ''
    }


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def index_page(request):
    context = get_base_context(request, 'Главная')

    return render(request, 'index.html', context)


def create_some_operators():
    a = Operator(name='Operator 1', website_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                 icon='operator_icons/icon1.jpg')
    a.save()
    b = Operator(name='Operator 2', website_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                 icon='operator_icons/icon2.jpg')
    b.save()
    c = Operator(name='Operator 3', website_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                 icon='operator_icons/icon3.jpg')
    c.save()


def create_some_tariffs():
    operators = Operator.objects.all()
    for _ in range(3):
        a = Tariff(cost=randint(MIN_PRICE, MAX_PRICE), minutes=randint(MIN_MINUTES, MAX_MINUTES),
                   internet=randint(MIN_GB, MAX_GB), messages=randint(MIN_MESSAGES, MAX_MESSAGES), operator=operators[0],
                   general_information='''Медве́жьи (лат. Ursidae) — семейство млекопитающих отряда хищных. Отличаются от других представителей псообразных более коренастым телосложением. Медведи всеядны, хорошо лазают и плавают, быстро бегают, могут стоять и проходить короткие расстояния на задних лапах. Имеют короткий хвост, длинную и густую шерсть, а также отличное обоняние. Охотятся вечером или на рассвете.''')
        a.save()
        a = Tariff(cost=randint(MIN_PRICE, MAX_PRICE), minutes=randint(MIN_MINUTES, MAX_MINUTES),
                   internet=randint(MIN_GB, MAX_GB), messages=randint(MIN_MESSAGES, MAX_MESSAGES), operator=operators[1],
                   general_information='''Волк, или се́рый волк, или обыкнове́нный волк (лат. Canis lupus), — вид хищных млекопитающих из семейства псовых (Canidae). Наряду с койотом (Canis latrans), обыкновенным шакалом (Canis aureus) и ещё несколькими видами составляет род волков (Canis). Кроме того, как показывают результаты изучения последовательности ДНК и дрейфа генов, является прямым предком домашней собаки (Canis familiaris; иногда классифицируется как подвид волка, Canis lupus familiaris).''')
        a.save()
        a = Tariff(cost=randint(MIN_PRICE, MAX_PRICE), minutes=randint(MIN_MINUTES, MAX_MINUTES),
                   internet=randint(MIN_GB, MAX_GB), messages=randint(MIN_MESSAGES, MAX_MESSAGES), operator=operators[2],
                   general_information='''Лиси́ца — это хищное млекопитающее, относится к отряду хищные, семейству псовые. В старославянском языке прилагательному «лисый» соответствовало определение желтоватого, рыжего и желтовато-оранжевого цвета, характерного для окраса широко распространенной лисы обыкновенной. Общее название нескольких видов млекопитающих семейства псовые. Только 10 видов этой группы относят к роду собственно лисиц (лат. Vulpes). Наиболее известный и распространённый представитель — обыкновенная лисица (Vulpes vulpes). Лисицы встречаются в фольклоре многих народов по всему миру.''')
        a.save()


def tariffs_page(request):
    context = get_base_context(request, 'Тарифы')

    context['MIN_PRICE'] = MIN_PRICE
    context['MIN_GB'] = MIN_GB
    context['MIN_MINUTES'] = MIN_MINUTES
    context['MIN_MESSAGES'] = MIN_MESSAGES
    context['MAX_PRICE'] = MAX_PRICE
    context['MAX_GB'] = MAX_GB
    context['MAX_MINUTES'] = MAX_MINUTES
    context['MAX_MESSAGES'] = MAX_MESSAGES

    tariffs = Tariff.objects.all()
    if not tariffs:
        create_some_operators()
        create_some_tariffs()
        tariffs = Tariff.objects.all()
    price = 0
    minutes = 0
    gb = 0
    messages = 0

    if request.method == 'GET' and 'price_input' in request.GET:
        price = int(request.GET['price_input'])
        minutes = int(request.GET['minutes_input'])
        gb = int(request.GET['gb_input'])
        messages = int(request.GET['messages_input'])

        tariffs_list = list(tariffs)
        tariffs_list.sort(key=lambda a: abs(price - a.cost)**2 + abs(minutes - a.minutes) + abs(gb - a.internet) + abs(messages - a.messages))
        tariffs = tariffs_list

    context['price_val'] = price
    context['minutes_val'] = minutes
    context['gb_val'] = gb
    context['messages_val'] = messages
    context['tariffs'] = tariffs
    return render(request, 'tariffs.html', context)


def tariff_page(request, id: int):
    context = get_base_context(request, 'Тариф')
    tariff = get_object_or_404(Tariff, id=id)
    if request.user.is_authenticated:
        cur_user = request.user.supplementeduser_set.first()
        isfavorite = Favorite_fact.objects.filter(tariff=tariff, fav_author=cur_user)
        context['isfavorite'] = isfavorite.count()
        print(isfavorite.count())

    if request.method == "POST" and request.user.is_authenticated:
        if "favorite" in request.POST:
            cur_user = request.user.supplementeduser_set.first()
            isfavorite = Favorite_fact.objects.filter(tariff=tariff, fav_author=cur_user)
            if isfavorite.count() == 0:
                favorite_cr = Favorite_fact(tariff=tariff, fav_author=cur_user)
                favorite_cr.save()
            else:
                Favorite_fact.objects.filter(id=isfavorite[0].id).delete()
        return redirect('/tariff/' + str(id))

    context['tariff'] = tariff
    return render(request, 'tariff_page.html', context)


def registration_page(request):
    context = get_base_context(request)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if not SupplementedUser.objects.filter(telephone_number=form.data['telephone_number']).exists():
                if not User.objects.filter(email=form.data['email']).exists():
                    if form.data['password'] == form.data['repeated_password']:
                        user1 = User()
                        user2 = SupplementedUser()
                        user1.set_password(raw_password=form.data['password'])
                        user1.first_name = form.data['first_name']
                        user1.last_name = form.data['last_name']
                        user1.email = form.data['email']
                        user2.date_of_birth = form.data['date_of_birth']
                        user2.telephone_number = form.data['telephone_number']
                        user2.patronymic = form.data['patronymic']
                        user1.username = len(SupplementedUser.objects.all())
                        user1.save()
                        user2.user = user1
                        user2.save()
                        login(request, user1)
                        return redirect(reverse('index'))
                    else:
                        form.add_error('repeated_password', 'Пароли не совпадают.')
                else:
                    form.add_error('email', 'Эта почта уже зарегистрирована')
            else:
                form.add_error('telephone_number', 'Этот номер телефона уже зарегистрирован.')
        else:
            form.add_error(None, 'Введённые данные некорректны.')
    context['form'] = form
    return render(request, 'registration.html', context)


def login_page(request):
    context = get_base_context(request, 'Вход')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.data
            email = data['email']
            password = data['password']
            user1 = User.objects.filter(email=email)
            if len(user1) == 0:
                form.add_error('email', 'Пользователь с email не зарегистрирован')
            elif check_password(password, user1[0].password):
                login(request, user1[0])
                return redirect(reverse('index'))
            else:
                form.add_error('password', 'Неверно введён пароль')
    context['form'] = form
    return render(request, 'login.html', context)


def profile_page(request):
    context = get_base_context(request, 'Профиль')
    if request.user.is_authenticated:
        current_user = get_object_or_404(SupplementedUser, user_id=request.user.id)
        context = get_base_context(request, 'Профиль')
        context['page_owner'] = current_user
        context['page_owner2'] = current_user.user
        context['u_id'] = current_user.id

        user1 = SupplementedUser.objects.get(user_id=request.user.id)
        favorits = Favorite_fact.objects.filter(fav_author=user1)
        any_objects = (Favorite_fact.objects.filter(fav_author=user1).count() > 0)
        context['any_objects'] = any_objects
        all_favs = []
        for i in favorits:
            all_favs.append(i.tariff)
        context['all_favs'] = all_favs
    else:
        return redirect('/login/')
    return render(request, 'profile.html', context)


def profile_edit_page(request):
    context = get_base_context(request, 'Пользовательские данные')
    form = FullPersonalInformationForm()
    if request.method == 'GET':
        try:
            user = get_object_or_404(SupplementedUser, user_id=request.user.id)
        except BaseException:
            form.add_error(None, 'incorrect session')
        else:
            user1 = SupplementedUser.objects.get(user_id=request.user.id)
            form = FullPersonalInformationForm(
                initial={
                    'date_of_birth': user.date_of_birth,
                    'email': request.user.email,
                    'name': request.user.first_name,
                    'surname': request.user.last_name,
                    'patronymic': user1.patronymic,
                    'telephone_number': user1.telephone_number,
                }
            )
            context['date_of_birth'] = f"{user.date_of_birth:%Y-%m-%d}"
    elif request.method == 'POST':
        form = FullPersonalInformationForm(request.POST, request.FILES)
        if form.is_valid():

                user_s = SupplementedUser.objects.get(user_id=request.user.id)
                data = form.data

                request.user.first_name = data['name']
                request.user.last_name = data['surname']
                request.user.email = data['email']
                user_s.telephone_number = data['telephone_number']
                user_s.patronymic = data['patronymic']
                user_s.date_of_birth = data['date_of_birth']
                request.user.save()
                user_s.save()

                return redirect('/profile/')

    context['form'] = form
    return render(request, 'profile_edit.html', context)


def password_change(request):
    context = get_base_context(request, 'Смена пароля')
    form = ChangePasswordForm()
    if request.method == 'GET':
        try:
            user = get_object_or_404(SupplementedUser, user_id=request.user.id)
        except BaseException:
            form.add_error(None, 'incorrect session')
        else:
            form = ChangePasswordForm()
    elif request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            try:
                user = get_object_or_404(SupplementedUser, user_id=request.user.id)
            except BaseException:
                form.add_error(None, 'incorrect session')
            else:
                old_password = request.POST.get("old_password")
                new_password = request.POST.get("new_password")
                rep_new_password = request.POST.get("rep_new_password")
                if not old_password or not new_password or not rep_new_password:
                    form.add_error(None, 'Одно из полей пустое')
                if check_password(old_password, user.user.password):
                    if new_password == rep_new_password:
                        if old_password == new_password:
                            form.add_error('new_password', 'Новый пароль должен отличаться от старого')
                        else:
                            name = request.user.username
                            request.user.set_password(new_password)
                            authenticate(username=name, password=new_password)
                            request.user.save()
                            return redirect(reverse('login'))
                    else:
                        form.add_error('rep_new_password', 'Введённые пароли не совпадают')
                else:
                    form.add_error('old_password', 'Старый пароль введён некорректно')
    context['form'] = form
    return render(request, 'password_change.html', context)




