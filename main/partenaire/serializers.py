from .models import Partenaire
from ..abstract.serializers import AbstractSerializer


class PartenaireSerializer(AbstractSerializer):
    class Meta:
        model = Partenaire
        fields = '__all__'
