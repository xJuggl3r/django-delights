from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from inventory.models import Ingredients, MenuItem, Purchase
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'home.html'


class InventoryView(ListView):
    model = Ingredients
    template_name = 'inventory.html'
    context_object_name = 'ingredients'


class CreateIngredientView(CreateView):
    model = Ingredients
    fields = '__all__'
    template_name = 'add_ingredient.html'
    success_url = reverse_lazy('inventory:index')


class UpdateIngredientView(UpdateView):
    model = Ingredients
    fields = ('name', 'quantity')
    template_name = 'edit_ingredient.html'
    success_url = reverse_lazy('inventory')


class DeleteIngredientView(DeleteView):
    model = Ingredients
    success_url = reverse_lazy('inventory')
    template_name = 'ingredient_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient'] = self.get_object()
        return context


class MenuView(ListView):
    model = MenuItem
    template_name = 'menu.html'
    context_object_name = 'menu_items'


class PurchaseView(ListView):
    model = Purchase
    template_name = 'purchases.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.annotate(total_price=F('quantity') * F('price'))


class ProfitView(TemplateView):
    template_name = 'profit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        menu_items = MenuItem.objects.all()

        revenue = 0
        cost = 0

        for purchase in purchases:
            revenue += purchase.total_price

        for menu_item in menu_items:
            cost += menu_item.price

        profit = revenue - cost
        context['revenue'] = revenue
        context['cost'] = cost
        context['profit'] = profit
        return context


class RecipeView(TemplateView):
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        return context
