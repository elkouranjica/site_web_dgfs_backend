from .models import Partenaire
from .serializers import PartenaireSerializer
from ..abstract.viewsets import AbstractViewSet
from rest_framework.permissions import AllowAny



class PartenaireViewSet(AbstractViewSet):
    queryset = Partenaire.objects.all()
    serializer_class = PartenaireSerializer
    permission_classes = (AllowAny,)
    http_method_names = 'get'

    def get_object(self):
        obj = Partenaire.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
