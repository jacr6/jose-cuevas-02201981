from django.shortcuts import render
from .models import Country
from .serializer import CountrySerializer
from rest_framework import viewsets

# Create your views here.


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer