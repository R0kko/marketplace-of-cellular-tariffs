"""marketplace_of_ct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import index_page, tariffs_page, registration_page, login_page, profile_page, profile_edit_page, \
    password_change, tariff_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('tariffs/', tariffs_page, name='tariffs'),
    path('tariff/<int:id>/', tariff_page, name='tariff_page'),
    path('registration/', registration_page, name='registration'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_page, name='my_profile'),
    path('profile/edit/', profile_edit_page, name='edit_page'),
    path('profile/edit/password_change', password_change, name='password_change'),

]
