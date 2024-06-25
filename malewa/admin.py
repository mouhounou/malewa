from django.contrib import admin
from . models import plat, boisson
# Register your models here.


class platAdmin(admin.ModelAdmin):
   liste_plat = ('name', 'priceM', 'priceL')
   
admin.site.register(plat, platAdmin)


class boissonAdmin(admin.ModelAdmin):
   liste_boisson = ('name', 'priceM', 'priceL')

admin.site.register(boisson, boissonAdmin)

