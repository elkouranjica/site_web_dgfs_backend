from django.contrib import admin
from django.db import models

from main.abstract.models import AbstractModel

CATEGORIE_PERSONNEL = [
    ('DE', "Directeur d'Etablissement"),
    ('DAT', "Directeur Adjoint Technique"),
    ('DAF', "Directeur Administratif et Financier"),
    ('INF', "Infirmier"),
    ('SF', "Sagefemme"),
    ('NA', "Non Attribué")
]


def logo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "logo_{0}/{1}".format(instance.public_id, filename)


class Etablissement(AbstractModel):
    name = models.CharField(max_length=200, unique=True)
    categorie = models.CharField(choices=[('ES', 'Etablissement Spécilaisé'),
                                          ('CHU', 'Centre Hospitalier Universitaire'),
                                          ('CHRR', 'Centre Hospitalier de Référence de Région'),
                                          ('CHRD', 'Centre Hospitalier de Référence de District'),
                                          ('CSB1', 'Centre de Santé de Base 1'),
                                          ('CSB2', 'Centre de Santé de Base 2')], max_length=4)
    adresse = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=logo_directory_path, null=True, blank=True)

    def __str__(self):
        return self.name


class Personnel(AbstractModel):
    etablissement = models.ForeignKey(Etablissement, related_name='personnels', on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    matricule = models.CharField(max_length=7, null=True, blank=True)
    categorie = models.CharField(max_length=3, choices=CATEGORIE_PERSONNEL, default='DE')
    photo = models.ImageField(upload_to='photo_DE', null=True, blank=True)

    def __str__(self):
        return self.nom + " " + self.prenom


class Description(AbstractModel):
    etablissement = models.ForeignKey(Etablissement, related_name='descriptions', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:20]

    # Reduire le nombre de texte sur le contenu dans Backend
    @admin.display(description="Contenu")
    def short_content(self):
        return self.content[:20] if self.content else ""


class Contact(AbstractModel):
    etablissement = models.ForeignKey(Etablissement, related_name='contacts', on_delete=models.CASCADE)
    contact_accueil = models.CharField(max_length=10, unique=True, null=True, blank=True)
    contact_urgence = models.CharField(max_length=10, unique=True, null=True, blank=True)
    contact_ambulance = models.CharField(max_length=10, unique=True, null=True, blank=True)
    contact_de = models.CharField(max_length=10, unique=True, null=True, blank=True)
    contact_daf = models.CharField(max_length=10, unique=True, null=True, blank=True)
    contact_dat = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return self.etablissement.name
    
    @admin.display(description="Accueil")
    def acceuil(self):
        return " ".join([self.contact_accueil[:3], self.contact_accueil[3:5], self.contact_accueil[5:8],
                         self.contact_accueil[8:]]) if self.contact_accueil else ""

    @admin.display(description="Urgence")
    def urgence(self):
        return " ".join([self.contact_urgence[:3], self.contact_urgence[3:5], self.contact_urgence[5:8],
                         self.contact_urgence[8:]]) if self.contact_urgence else ""

    @admin.display(description="Ambulance")
    def ambulance(self):
        return " ".join([self.contact_ambulance[:3], self.contact_ambulance[3:5], self.contact_ambulance[5:8],
                         self.contact_ambulance[8:]]) if self.contact_ambulance else ""

    @admin.display(description="DE")
    def de(self):
        return " ".join([self.contact_de[:3], self.contact_de[3:5], self.contact_de[5:8],
                         self.contact_de[8:]]) if self.contact_de else ""

    @admin.display(description="DAF")
    def daf(self):
        return " ".join([self.contact_daf[:3], self.contact_daf[3:5], self.contact_daf[5:8],
                         self.contact_daf[8:]]) if self.contact_daf else ""

    @admin.display(description="DAT")
    def dat(self):
        return " ".join([self.contact_dat[:3], self.contact_dat[3:5], self.contact_dat[5:8],
                         self.contact_dat[8:]]) if self.contact_dat else ""


# Service : ex = ORL, Maternité, Pédiatrie, ...
class Service(AbstractModel):
    etablissement = models.ForeignKey(Etablissement, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        unique_together = ('name', 'etablissement')

    def __str__(self):
        return self.name
