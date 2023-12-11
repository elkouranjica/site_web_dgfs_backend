from rest_framework.permissions import AllowAny

from main.abstract.viewsets import AbstractViewSet
from main.etablissement.models import Etablissement
from main.etablissement.serializers.etablissement import EtablissementSerializer


class EtablissementViewSet(AbstractViewSet):
    http_method_names = "get"
    permission_classes = (AllowAny,)
    serializer_class = EtablissementSerializer
    queryset = Etablissement.objects.all()

    def get_object(self):
        obj = Etablissement.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
