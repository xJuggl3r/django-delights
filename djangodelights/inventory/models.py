from django.db import models


# Create your models here.


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0.0)


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='menu_images/', blank=True)
    recipe_url = models.URLField(blank=True)

    # return a string representation of the object
    def __str__(self):
        return self.title


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(
        "inventory.MenuItem", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        "inventory.Ingredients", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        ingredient = RecipeRequirement.objects.get(
            menu_item=self.menu_item).ingredient
        self.price = ingredient.price_per_unit
        self.purchase_total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    @property
    def purchase_total_price(self):
        return self.price * self.quantity
