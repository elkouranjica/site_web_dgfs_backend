from rest_framework.permissions import AllowAny
from main.abstract.viewsets import AbstractViewSet
from main.institution.models import Ministere, Direction, Service, \
    Directeur, ChefService
from main.institution.serializers import MinistereSerializer, \
    DirectionCentraleSerializer, ServiceSerializer, \
    DirecteurSerializer, ChefServiceSerializer


class MinistereViewSet(AbstractViewSet):
    queryset = Ministere.objects.all()
    serializer_class = MinistereSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = Ministere.objects.get_object_by_public_id(
            self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class DirectionViewSet(AbstractViewSet):
    queryset = Direction.objects.filter(type_direction='DC')
    serializer_class = DirectionCentraleSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = Direction.objects.get_object_by_public_id(
            self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class ServiceViewSet(AbstractViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = Service.objects.get_object_by_public_id(
            self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class DirecteurViewSet(AbstractViewSet):
    queryset = Directeur.objects.all()
    serializer_class = DirecteurSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = Directeur.objects.get_object_by_public_id(
            self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class ChefServiceViewSet(AbstractViewSet):
    queryset = ChefService.objects.all()
    serializer_class = ChefServiceSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = ChefService.objects.get_object_by_public_id(
            self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
