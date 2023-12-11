from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Etablissement)
class EtablissementAdmin(ModelAdmin):
    list_display = ["name", "categorie", "adresse", "logo"]
    list_filter = ["categorie"]
    ordering = ["name"]
    search_fields = ["name"]


@admin.register(Personnel)
class PersonnelAdmin(ModelAdmin):
    list_display = ["matricule", "nom", "prenom"]
    list_filter = ["etablissement", "categorie"]
    search_fields = ["matricule", "nom", "prenom"]
    ordering = ["matricule"]


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ["etablissement", "name"]
    list_filter = ["etablissement"]
    ordering = ["etablissement"]
    search_fields = ["name"]


@admin.register(Description)
class DescriptionAdmin(ModelAdmin):
    list_display = ["etablissement", "short_content"]
    list_filter = ["etablissement"]


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ["etablissement", "de", "dat", "daf", "acceuil", "urgence", "ambulance"]
    list_filter = ["etablissement"]
    ordering = ["etablissement"]
    search_fields = ["etablissement"]

