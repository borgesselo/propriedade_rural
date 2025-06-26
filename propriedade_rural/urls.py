from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TipoInsumoViewSet

router = DefaultRouter()
router.register(r'TipoInsumo', TipoInsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import insumoViewSet

router = DefaultRouter()
router.register(r'insumos', insumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import culturaViewSet

router = DefaultRouter()
router.register(r'culturas', culturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import propriedadesViewSet

router = DefaultRouter()
router.register(r'propriedades', propriedadesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import cargoViewSet

router = DefaultRouter()
router.register(r'cargos', cargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import funcionarioViewSet

router = DefaultRouter()
router.register(r'funcionarios', funcionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import plantioViewSet

router = DefaultRouter()
router.register(r'plantio', plantioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import colheitaViewSet

router = DefaultRouter()
router.register(r'colheitas', colheitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import usoinsumoViewSet

router = DefaultRouter()
router.register(r'usoinsumo', usoinsumoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]