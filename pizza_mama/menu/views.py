from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def index(request):
    # pizzas = Pizza.objects.all()
    # pizzas_names_and_prices = [f"{i}. {pizza.name.capitalize()} -- {pizza.price} €" for i, pizza in enumerate(pizzas, start=1)]
    # return HttpResponse("Les pizzas disponibles sont :</br></br>" + "</br>".join(pizzas_names_and_prices))
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})