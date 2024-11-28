from django.contrib import admin
from django.urls import path, include
from produtos.views import cadastro_produto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', include('produtos.urls'))

]
