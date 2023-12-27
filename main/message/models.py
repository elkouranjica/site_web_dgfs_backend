from django.db import models
from main.abstract.models import AbstractModel


class Message(AbstractModel):
    mail_address = models.CharField(max_length=200)
    mail_object = models.CharField(max_length=200)
    mail_content = models.TextField()

    def __str__(self):
        return self.mail_address
