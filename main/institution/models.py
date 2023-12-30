from django.db import models
from main.abstract.models import AbstractModel


class Ministere(AbstractModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Direction(AbstractModel):
    name = models.CharField(max_length=255)
    type_direction = models.CharField(choices=[('DG', 'Direction Générale'), ('DC', 'Direction Centrale'),
                                               ('DirCab', 'Direction des membres du Cabinet')], default='DC',
                                      max_length=6)
    accronyme = models.CharField(max_length=20, null=True, blank=True)
    direction_generale = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                           limit_choices_to={'type_direction': 'DG'})
    ministere = models.ForeignKey(Ministere, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'ministere')

    def __str__(self):
        return str(self.name).title()


class Service(AbstractModel):
    name = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    accronyme = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Directeur(AbstractModel):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=6)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom).upper() + " " + str(self.prenom).title()


class ChefService(AbstractModel):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=6)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom).upper() + " " + str(self.prenom).title()
