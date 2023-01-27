from django.urls import path, include

from .views import IndexView, InventoryView, CreateIngredientView, UpdateIngredientView, DeleteIngredientView, MenuView, PurchaseView, ProfitView, RecipeView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'inventory'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('add_ingredient/', CreateIngredientView.as_view(), name='add_ingredient'),
    path('edit_ingredient/<int:pk>/',
         UpdateIngredientView.as_view(), name='edit_ingredient'),
    path('inventory/<int:pk>/delete/',
         DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('purchases/', PurchaseView.as_view(), name='purchases'),
    path('profit/', ProfitView.as_view(), name='profit'),
    path('recipe/', RecipeView.as_view(), name='recipe'),
]


# """Remember: In production, you should configure your web server to serve static files directly instead of relying on Django to serve them.
# # Nginx: In your Nginx configuration file, add the following lines:

# location /media/ {
#   alias /path/to/your/media/root/;
# }

# location /static/ {
#   alias /path/to/your/static/root/;
# }
# """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
