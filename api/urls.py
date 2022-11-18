from django.urls import path
from api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('<str:text>', views.FindDomainView.as_view(), name='domain'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/', 
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    )
]