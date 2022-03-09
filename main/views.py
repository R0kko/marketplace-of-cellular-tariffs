from django.shortcuts import render, get_object_or_404
from main.models import Tariff

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


def tariff_page(request, id: int):
    context = {}
    tariff = get_object_or_404(Tariff, id=id)
    context['tariff'] = tariff
    return render(request, 'tariff_page.html', context)