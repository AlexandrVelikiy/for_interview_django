from django.contrib import admin

from pizza.models import Pizza, Ingredient, IngredientType

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(IngredientType)

