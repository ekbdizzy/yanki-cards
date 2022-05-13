from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Yanki cards API",
        default_version='v1',
        description="This API is used only to simplify development. "
        "It's not available with production settings.",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(
        'swagger(?<format>.json|.yaml)',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]
