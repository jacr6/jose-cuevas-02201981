from django.contrib import admin
from django.apps import apps
from .models import Country

# all other models
adminmodels = apps.get_models()
 
class CountryAdmin(admin.ModelAdmin):
      # A handy constant for the name of the alternate database.
    using = 'EveryMundo'
 
    
    # def save_model(self, request, obj, form, change):
    #     # Tell Django to save objects to the 'mssql' database.
    #     obj.save(using=self.using)

    # def delete_model(self, request, obj):
    #     # Tell Django to delete objects from the 'mssql' database
    #     obj.delete(using=self.using)

    # def get_queryset(self, request):
    #     # Tell Django to look for objects on the 'mssql' database.
    #     return super().get_queryset(request).using(self.using)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     # Tell Django to populate ForeignKey widgets using a query
    #     # on the 'mssql' database.
    #     return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     # Tell Django to populate ManyToMany widgets using a query
    #     # on the 'mssql' database.
    #     return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
        
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