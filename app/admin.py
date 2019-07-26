from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Pocket)
class PocketAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'initial_amount',
        'spend',
        'amount',
        'date_one',
        'date_two',
        'user'
    ]


@admin.register(models.CurentSpend)
class CurentSpendAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'amount',
        'register',
        'pocket'
    ]
