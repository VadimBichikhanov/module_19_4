from django.contrib import admin
from .models import Buyer, Game

# Настройка админ-класса для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение количества записей до 20

# Настройка админ-класса для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение количества записей до 30
    readonly_fields = ('balance',)
    
fieldsets = (
    (None, {
        "fields": (
            "name",
            "balance",
            "age",
        ),
    }),
    ("Дополнительная информация", {
        "classes": ("collapse",),
        "fields": (
            "registration_date",
        ),
    }),
)
readonly_fields = ("registration_date",)