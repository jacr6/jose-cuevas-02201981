from django.urls import path, include
from django.contrib import admin
from countries.api import CountryCreateApi, CountryApi, CountryUpdateApi, CountryDeleteApi


urlpatterns = [
    path('Countries', CountryApi.as_view()),
    path('Country/create', CountryCreateApi.as_view()),
    path('Country/<name>', CountryUpdateApi.as_view()),
    path('Country/<name>/delete',CountryDeleteApi.as_view()),
    path('admin/', admin.site.urls),
]
