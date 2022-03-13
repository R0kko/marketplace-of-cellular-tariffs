from main.models import Tariff, Operator
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index_page(request):
    context = {}

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
    a = Tariff(cost=120, minutes=300, internet=5, messages=10, operator=operators[0],
               general_information='''Пользоваться мессенджерами в поездках можно безлимитно. В тариф включены услуги «Безлимитные
                    мессенджеры за границей» и «Безлимитные мессенджеры на полуострове» на специальных условиях:
                    оплачивайте тариф вовремя и пользуйтесь услугами бесплатно. Находясь за границей или в Республике
                    Крым и г. Севастополь без подключения дополнительных опций, безлимитно предоставляется доступ к
                    Viber, ТамТам, WhatsApp, а исходящие звонки на Tele2 России из популярных стран Европы включены
                    в пакет тарифа.''')
    a.save()
    b = Tariff(cost=123, minutes=321, internet=1, messages=0, operator=operators[1])
    b.save()
    c = Tariff(cost=666, minutes=666, internet=666, messages=666, operator=operators[2])
    c.save()


def tariffs_page(request):
    context = {}
    tariffs = Tariff.objects.all()
    if not tariffs:
        create_some_operators()
        create_some_tariffs()
        tariffs = Tariff.objects.all()

    if request.method == 'GET':
        print(request.GET)

    context['tariffs'] = tariffs
    return render(request, 'tariffs.html', context)


def tariff_page(request, id: int):
    context = {}
    tariff = get_object_or_404(Tariff, id=id)
    context['tariff'] = tariff
    return render(request, 'tariff_page.html', context)