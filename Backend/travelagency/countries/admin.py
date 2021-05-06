from django.contrib import admin
from django.apps import apps
from .models import Country

# all other models
adminmodels = apps.get_models()
 
class CountryAdmin(admin.ModelAdmin):
      # A handy constant for the name of the alternate database.
    using = 'EveryMundo'
  
    list_filter = ('name', 'currency', 'locale')
    list_display = ('name', 'currency', 'locale')
    search_fields = ('name', 'currency', 'locale')

    pass
admin.site.register(Country, CountryAdmin)

for model in adminmodels:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass