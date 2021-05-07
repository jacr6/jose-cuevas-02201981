from rest_framework import generics
from rest_framework.response import Response
from .serializer import CountrySerializer
from .models import Country


class CountryCreateApi(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryApi(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryFindApi(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    lookup_field = 'name'
    serializer_class = CountrySerializer


class CountryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    lookup_field = 'name'
    serializer_class = CountrySerializer


class CountryDeleteApi(generics.DestroyAPIView):
    queryset = Country.objects.all()
    lookup_field = 'name'
    serializer_class = CountrySerializer
