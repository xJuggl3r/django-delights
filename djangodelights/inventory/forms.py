from django import forms
from .models import Ingredients, MenuItem, RecipeRequirement, Purchase

# CRUD - Create


class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ('ingredient', 'quantity', 'unit', 'price_per_unit')


class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price')


class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'timestamp')

# CRUD - Update


class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ('ingredient', 'quantity', 'unit', 'price_per_unit')


class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price')


class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')


class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'timestamp')
