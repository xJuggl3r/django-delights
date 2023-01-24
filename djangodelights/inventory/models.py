from django.db import models

# Create your models here.


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unity = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0.0)


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(
        "inventory.MenuItem", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        "inventory.Ingredients", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


class Purchase(models.Model):
    menu_item = models.ForeignKey(
        "inventory.MenuItem", on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
