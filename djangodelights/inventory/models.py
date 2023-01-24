from django.db import models

# Create your models here.


class Ingredients(models.Model):
    pass
    ingredient = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    price_per_unit = models.FloatField(default=0.0)


class MenuItem(models.Model):
    pass


class RecipeRequirement(models.Model):
    pass


class Purchase(models.Model):
    pass
