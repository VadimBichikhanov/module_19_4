"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.urls import path, include
from task1 import views  # Импортируем представление для домашней страницы и других представлений
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'buyers', views.BuyerViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляем URL-адреса аутентификации
    path('', views.home, name='home'),  # Добавляем маршрут для домашней страницы
    path('registration/', views.registration, name='registration'),  # Добавляем маршрут для регистрации
    path('product_list/', views.product_list, name='product_list'),  # Добавляем маршрут для списка товаров
    path('shop/', views.shop, name='shop'),  # Добавляем маршрут для магазина
    path('contact/', views.contact, name='contact'),  # Добавляем маршрут для контактов
    path('about/', views.about, name='about'),  # Добавляем маршрут для информации о нас
    path('cart/', views.cart, name='cart'),  # Добавляем маршрут для корзины
    path('choice_page/', views.choice_page, name='choice_page'),  # Добавляем маршрут для выбора регистрации
    path('sign_up_by_django/', views.sign_up_by_django, name='sign_up_by_django'),  # Добавляем маршрут для регистрации через Django
    path('login/', views.login_view, name='login'),  # Добавляем маршрут для входа
    path('logout/', views.logout_view, name='logout'),  # Добавляем маршрут для выхода
    path('api/', include(router.urls)),  # Добавляем маршруты для API
]