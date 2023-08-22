from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

from usuario.router import router as usuario_router
from garagem.views import (
    MarcaViewSet,
    CategoriaViewSet,
    CorViewSet,
    AcessorioViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"Categorias", CategoriaViewSet)
router.register(r"Cores", CorViewSet)
router.register(r"Acessorios", AcessorioViewSet)
router.register(r"Veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("", include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
