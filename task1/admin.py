from django.contrib import admin
from .models import Game, Buyer

# Админ-класс для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение количества записей до 20

    fieldsets = (
        (None, {
            "fields": (
                'title', 'cost', 'size'
            ),
        }),
        ('Дополнительные настройки',{
            'classes':('colapse',),
            "fields":('title', 'cost', 'size')
        })
    )
    

# Админ-класс для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение количества записей до 30
    readonly_fields = ('balance',)  # Поле balance доступно только для чтения
    
    fieldsets = (
        (None, {
            "fields": ('balance', 'age', 'name',),
        }),
        ('Дополнительные настройки', {
            'classes':('colapse',),
            'fields':('name', 'balance', 'age')
        })
    )
    