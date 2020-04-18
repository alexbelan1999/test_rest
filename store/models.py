from django.db import models


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    card_number = models.IntegerField()
    csv = models.IntegerField()
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account'

    def __str__(self):
        return str(self.id)

class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    calorie = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ingredient'


class Recipes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    recipe = models.TextField()

    class Meta:
        managed = False
        db_table = 'recipes'


class RecipesIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe = models.ForeignKey(Recipes, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    gram = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recipes_ingredient'


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    ingridient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'store'

    def __str__(self):
        return str(self.id)

class Transfers(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(Account, models.DO_NOTHING, related_name="sender")
    recipient = models.ForeignKey(Account, models.DO_NOTHING, related_name="recipient")
    sum = models.FloatField()
    transfer_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transfers'

    def __str__(self):
        return str(self.id)

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    patronymic = models.CharField(max_length=25, blank=True, null=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    account = models.ForeignKey(Account, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.surname + ' '+ self.name