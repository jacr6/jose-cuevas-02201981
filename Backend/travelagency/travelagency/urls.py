from django.urls import path, include
from djongo.models import * 
from rest_framework import routers, serializers, viewsets
from django.contrib import admin


 
# # Serializers define the API representation.
# class EveryMundoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = EveryMundo
#         fields = [
#             "name",
#             "currency",
#             "symbol",
#             "centseparator",
#             "millionseparator",
#             "locale",
#             "decimals",
#             "displaysymbol"
#         ]

# # ViewSets define the view behavior.


# class EveryMundoViewSet(viewsets.ModelViewSet):
#     queryset = EveryMundo.objects.all()
#     serializer_class = EveryMundoSerializer


# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'EveryMundos', EveryMundoViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

 
