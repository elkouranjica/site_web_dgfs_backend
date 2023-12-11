from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.http import Http404

from main.abstract.models import AbstractModel


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.public_id, filename)


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, matricule, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not matricule:
            raise ValueError("L'utilisateur doit fournir son matricule")

        user = self.model(
            matricule=matricule,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricule, password=None):
        user = self.create_user(
            matricule,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, AbstractModel):
    matricule = models.CharField(
        db_index=True,
        verbose_name="Matricule",
        max_length=6,
        unique=True,
    )
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    categorie = models.CharField(choices=[('Dr', 'Docteur'), ('Pr', 'Professeur'), ('Sf', 'Sagefemme'),
                                          ('Inf', 'Infirmier'), ('Ad', 'Administratif'), ('PA', 'Personnel d\'appui')],
                                 max_length=3, null=True)

    objects = UserManager()

    USERNAME_FIELD = "matricule"

    def __str__(self):
        return self.matricule

    @property
    def name(self):
        return f"{self.first_name.title()} {self.last_name.upper()}"

    @staticmethod
    def has_perm(perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
