from django.shortcuts import render
from django.contrib.auth.models import User
from main.forms import RegistrationForm, LoginForm, FullPersonalInformationForm, ChangePasswordForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import check_password

from main.models import SupplementedUser, Notification, Tariff


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


def create_some_tariffs():
    a = Tariff(cost = 120, minutes = 300, internet = 5, messages = 10)
    a.save()
    b = Tariff(cost=123, minutes=321, internet=1, messages=0)
    b.save()
    c = Tariff(cost=666, minutes=666, internet=666, messages=666)
    c.save()


def tariffs_page(request):
    context = {}
    tariffs = Tariff.objects.all()
    if not tariffs:
        create_some_tariffs()
        tariffs = Tariff.objects.all()

    context['tariffs'] = tariffs
    return render(request, 'tariffs.html', context)


def registration_page(request):
    context = get_base_context(request)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if not SupplementedUser.objects.filter(telephone_number=form.data['telephone_number']).exists():
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
                    user1.save()
                    user2.user = user1
                    user2.save()
                    login(request, user1)
                    return redirect(reverse('index'))
                else:
                    form.add_error('repeated_password', 'Пароли не совпадают.')
            else:
                form.add_error('telephone_number', 'Этот номер уже зарегистрирован.')
        else:
            form.add_error(None, 'Введённые данные некорректны.')
    context['form'] = form
    return render(request, 'registration.html', context)


def login_page(request):
    context = get_base_context(request)
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.data
            email = data['email']
            password = data['password']
            user1 = User.objects.filter(email=email)
            if len(user1) == 0:
                form.add_error('telephone_number', 'Пользователь с email не зарегистрирован')
            if check_password(password, user1[0].password):
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
            user1 = SupplementedUser.objects.filter(user_id=request.user.id)[0]
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
            try:
                user = get_object_or_404(SupplementedUser, user_id=request.user.id)
            except BaseException:
                form.add_error(None, 'incorrect session')
            else:
                data = form.data
                instance = form.instance

                request.user.first_name = data['name']
                request.user.last_name = data['surname']
                request.user.email = data['email']
                request.user.save()

                user.date_of_birth = instance.date_of_birth
                user.save()
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




