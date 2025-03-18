from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Incluye las rutas de home
    #path('usuarios/', include('usuarios.urls')),  # Incluye las rutas de usuarios
    path('productos/', include('productos.urls')),  # Incluye las rutas de productos
]
