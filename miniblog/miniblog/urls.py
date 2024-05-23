from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("home.urls"), name = 'index'),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
]