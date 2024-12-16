# task1/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Buyer, Game
from .forms import RegistrationForm, LoginForm
from .serializers import BuyerSerializer, GameSerializer
from rest_framework import viewsets
from django.contrib import messages

def home(request):
    # Получаем всех покупателей из базы данных
    buyers = Buyer.objects.all()
    # Передаем данные в шаблон
    return render(request, 'home.html', {'buyers': buyers})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка совпадения паролей
            if password != repeat_password:
                form.add_error('repeat_password', 'Пароли не совпадают')
                return render(request, 'registration.html', {'form': form})

            # Проверка существования пользователя
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Пользователь уже существует')
                return render(request, 'registration.html', {'form': form})

            if Buyer.objects.filter(name=username).exists():
                form.add_error('username', 'Пользователь уже существует в таблице Buyer')
                return render(request, 'registration.html', {'form': form})

            # Создание пользователя
            User.objects.create_user(username=username, password=password)
            Buyer.objects.create(name=username, age=age)
            return redirect('login')
    else:
        form = RegistrationForm()

    buyers = Buyer.objects.all()
    return render(request, 'registration.html', {'form': form, 'buyers': buyers})

def product_list(request):
    games = Game.objects.all()
    return render(request, 'product_list.html', {'games': games})

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def choice_page(request):
    return render(request, 'choice_page.html')

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                info['form'] = form
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            elif User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует в таблице Buyer'
            else:
                # Создание нового пользователя
                User.objects.create_user(username=username, password=password)
                Buyer.objects.create(name=username, age=age)
                return redirect('login')
    else:
        form = RegistrationForm()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})




def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return redirect('home')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer