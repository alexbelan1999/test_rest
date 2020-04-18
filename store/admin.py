from django.contrib import admin
from .models import Account,Ingredient,Recipes,RecipesIngredient,Store,Transfers,Users

admin.site.register(Account)
admin.site.register(Ingredient)
admin.site.register(Recipes)
admin.site.register(RecipesIngredient)
admin.site.register(Store)
admin.site.register(Transfers)
admin.site.register(Users)
