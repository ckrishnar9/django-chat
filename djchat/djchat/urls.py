from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from server.views import ServerListViewSet

router = DefaultRouter()
router.register("api/server/select", ServerListViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    