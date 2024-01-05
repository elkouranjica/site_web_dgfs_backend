from rest_framework import serializers
from main.abstract.serializers import AbstractSerializer

from main.institution.models import Ministere, Direction, Service, \
    Directeur, ChefService


class MinistereSerializer(AbstractSerializer):
    class Meta:
        model = Ministere
        fields = '__all__'


class DirectionSerializer(AbstractSerializer):
    class Meta:
        model = Direction
        fields = '__all__'



class DirectionCentraleSerializer(AbstractSerializer):
    class Meta:
        model = Direction
        fields = "__all__"



class ServiceSerializer(AbstractSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class DirecteurSerializer(AbstractSerializer):
    class Meta:
        model = Directeur
        fields = '__all__'


class ChefServiceSerializer(AbstractSerializer):
    class Meta:
        model = ChefService
        fields = '__all__'
