from django import forms
from .models import SupplementedUser

class RegistrationForm(forms.Form):
    telephone_number = forms.CharField(max_length=18, min_length=1, required=True, label='Номер', widget=forms.TextInput())
    first_name = forms.CharField(max_length=150, min_length=1, required=True, label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(max_length=150, min_length=1, required=True, label='Фамилия', widget=forms.TextInput())
    patronymic = forms.CharField(max_length=150, min_length=1, required=True, label='Отчество', widget=forms.TextInput())
    email = forms.CharField(max_length=150, min_length=1, required=True, label='Почта', widget=forms.EmailInput())
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput())
    password = forms.CharField(max_length=128, min_length=1, required=True,
                               label='Придумайте новый пароль', widget=forms.PasswordInput())
    repeated_password = forms.CharField(max_length=128, min_length=1, required=True,
                                        label='Повторите пароль', widget=forms.PasswordInput())

class FullPersonalInformationForm(forms.ModelForm):
    name = forms.CharField(max_length=150, min_length=1, required=True, label='Имя', widget=forms.TextInput())
    surname = forms.CharField(max_length=150, min_length=1, required=True, label='Фамилия', widget=forms.TextInput())
    patronymic = forms.CharField(max_length=150, min_length=1, required=True, label='Отчество', widget=forms.TextInput())
    telephone_number = forms.CharField(max_length=14, min_length=1, required=True, label='Номер телефона', widget=forms.TextInput())
    email = forms.CharField(max_length=150, min_length=1, required=True, label='Почта', widget=forms.TextInput())
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput())

    class Meta:
        model = SupplementedUser
        fields = ('name', 'surname', 'patronymic', 'telephone_number', 'email', 'date_of_birth')


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=150, min_length=1, required=True, label='Старый пароль', widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=150, min_length=1, required=True, label='Новый пароль', widget=forms.PasswordInput())
    rep_new_password = forms.CharField(max_length=150, min_length=1, required=True, label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = SupplementedUser
        fields = ('old_password', 'new_password', 'rep_new_password')



class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, min_length=1, required=True, label='Email', widget=forms.TextInput())
    password = forms.CharField(max_length=128, min_length=1, required=True,
                               label='Введите пароль', widget=forms.PasswordInput())
