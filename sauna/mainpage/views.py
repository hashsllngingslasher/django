
from django.shortcuts import render
from mainpage.models import ServiceCategory, Service


def index(request):
    context = {
        'title': 'Bathhouse'
    }
    return render(request, 'mainpage/index.html', context)


def services(request):
    context = {
        'title': 'Type of Bath',
        'baths': Service.objects.all(),
        'categories': ServiceCategory.objects.all(),
    }
    return render(request, 'mainpage/price.html', context)
