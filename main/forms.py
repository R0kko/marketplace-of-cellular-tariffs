from django import forms
from .models import SupplementedUser

class RegistrationForm(forms.Form):
    telephone_number = forms.CharField(max_length=18, min_length=1, required=True, label='Номер', widget=forms.TextInput())
    first_name = forms.CharField(max_length=150, min_length=1, required=True, label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(max_length=150, min_length=1, required=True, label='Фамилия', widget=forms.TextInput())
    password = forms.CharField(max_length=128, min_length=1, required=True,
                               label='Придумайте новый пароль', widget=forms.PasswordInput())
    repeated_password = forms.CharField(max_length=128, min_length=1, required=True,
                                        label='Повторите пароль', widget=forms.PasswordInput())