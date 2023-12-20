from rest_framework import serializers

from main.abstract.serializers import AbstractSerializer
from main.etablissement.models import Etablissement, Description, Service, Personnel, Contact


class DescriptionSerializer(AbstractSerializer):
    class Meta:
        model = Description
        fields = ["content", "updated"]


class ServiceSerializer(AbstractSerializer):
    class Meta:
        model = Service
        fields = ["name"]


class PersonnelSerializer(AbstractSerializer):
    class Meta:
        model = Personnel
        fields = ["nom", "prenom", "categorie", "matricule", "photo"]


class ContactSerializer(AbstractSerializer):
    class Meta:
        model = Contact
        fields = ["contact_accueil", "contact_urgence", "contact_ambulance", "contact_de", "contact_dat",
                  "contact_daf"]


class EtablissementSerializer(AbstractSerializer):
    descriptions = DescriptionSerializer(many=True)
    services = ServiceSerializer(many=True)
    contacts = ContactSerializer(many=True)
    directeur = serializers.SerializerMethodField()

    class Meta:
        model = Etablissement
        fields = ["id", "name", "categorie", "adresse", "logo", "descriptions", "services", "directeur", "contacts" , "image"]

    @staticmethod
    def get_directeur(obj):
        # Récupérer le directeur associé à l'établissement avec catégorie 'DE'
        directeur_instance = Personnel.objects.filter(etablissement=obj, categorie='DE').first()

        if directeur_instance:
            directeur_serializer = PersonnelSerializer(directeur_instance)
            return directeur_serializer.data
        return None
