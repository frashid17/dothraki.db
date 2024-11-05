from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Fahim, Mumina, Nickson, Ahlam, Ashley, Patel

# Create a resource class for each model
class FahimResource(resources.ModelResource):
    class Meta:
        model = Fahim

class MuminaResource(resources.ModelResource):
    class Meta:
        model = Mumina

class NicksonResource(resources.ModelResource):
    class Meta:
        model = Nickson

class AhlamResource(resources.ModelResource):
    class Meta:
        model = Ahlam

class AshleyResource(resources.ModelResource):
    class Meta:
        model = Ashley

class PatelResource(resources.ModelResource):
    class Meta:
        model = Patel

# Create an ImportExportModelAdmin for each model
@admin.register(Fahim)
class FahimAdmin(ImportExportModelAdmin):
    resource_class = FahimResource
    list_display = ("firstname", "lastname", "date_added")

@admin.register(Mumina)
class MuminaAdmin(ImportExportModelAdmin):
    resource_class = MuminaResource
    list_display = ("firstname", "lastname", "date_added")

@admin.register(Nickson)
class NicksonAdmin(ImportExportModelAdmin):
    resource_class = NicksonResource
    list_display = ("firstname", "lastname", "date_added")

@admin.register(Ahlam)
class AhlamAdmin(ImportExportModelAdmin):
    resource_class = AhlamResource
    list_display = ("firstname", "lastname", "date_added")

@admin.register(Ashley)
class AshleyAdmin(ImportExportModelAdmin):
    resource_class = AshleyResource
    list_display = ("firstname", "lastname", "date_added")

@admin.register(Patel)
class PatelAdmin(ImportExportModelAdmin):
    resource_class = PatelResource
    list_display = ("firstname", "lastname", "date_added")
