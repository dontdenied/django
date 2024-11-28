from django.contrib import admin
from django.urls import path
from produtos.views import cadastro_produto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', cadastro_produto)

]
