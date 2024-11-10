from django.shortcuts import render
from .models import Buyer, Game

def create_records(request):
    # Создаем записи Buyer
    buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=25)
    buyer2 = Buyer.objects.create(name='Bob', balance=150.00, age=30)
    buyer3 = Buyer.objects.create(name='Charlie', balance=200.00, age=16)

    # Создаем записи Game
    game1 = Game.objects.create(title='Game1', cost=50.00, size=2.5, description='Description1', age_limited=True)
    game2 = Game.objects.create(title='Game2', cost=30.00, size=1.5, description='Description2', age_limited=False)
    game3 = Game.objects.create(title='Game3', cost=40.00, size=2.0, description='Description3', age_limited=True)

    # Связываем игры с покупателями
    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    return render(request, 'records_created.html')

def home(request):
    return render(request, 'home.html')