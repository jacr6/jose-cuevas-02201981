from django.urls import path, include
from django.contrib import admin
from countries.api import CountryCreateApi, CountryApi, CountryUpdateApi, CountryDeleteApi
from countries.views import CountryViewSet
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title='Countries API')


router = routers.DefaultRouter()
router.register(r'', CountryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    url(r'swagger', schema_view),
    path('Countries', CountryApi.as_view()),
    path('Country/create', CountryCreateApi.as_view()),
    path('Country/<name>', CountryUpdateApi.as_view()),
    path('Country/<name>/delete', CountryDeleteApi.as_view()),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)