from django.shortcuts import render
from django.contrib.auth.models import User
from main.forms import RegistrationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from main.models import SupplementedUser, Notification, Tariff


# Create your views here.


def index_page(request):
    context = {}

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

def get_base_context(request, pagename: str = "Page"):
    user = SupplementedUser.objects.filter(user_id=request.user.id).first()
    if user:
        user.new_notifications_count = len(Notification.objects.filter(receiver=user))
        user.save()
    return {
        'is_authenticated': request.user.is_authenticated,
        'pagename': pagename,
        'User': get_object_or_404(SupplementedUser, user_id=request.user.id) if request.user.is_authenticated else '',
    }


def registration_page(request):
    context = get_base_context(request)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=form.data['username']).exists():
                if form.data['password'] == form.data['repeated_password']:
                    user = User(username=form.data['username'])
                    user.set_password(raw_password=form.data['password'])
                    user.first_name = form.data['first_name']
                    user.last_name = form.data['last_name']
                    user.save()
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    form.add_error('repeated_password', 'Пароли не совпадают.')
            else:
                form.add_error('username', 'Этот номер уже зарегестрирован.')
        else:
            form.add_error(None, 'Введённые данные некорректны.')
    context['form'] = form
    return render(request, 'registration.html', context)

