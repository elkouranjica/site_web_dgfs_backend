from django.db import models
from main.abstract.models import AbstractModel


def logo_directory_path(instance, filename):
    return "logo_{0}/{1}".format(instance.public_id, filename)


class Partenaire(AbstractModel):
    name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to=logo_directory_path, null=True, blank=True)
    lien_page = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
