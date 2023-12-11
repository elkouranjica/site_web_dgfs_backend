from rest_framework.permissions import IsAuthenticated

from main.abstract.viewsets import AbstractViewSet
from main.user.serializers import UserSerializer
from main.user.models import User


class UserViewSet(AbstractViewSet):
    http_method_names = ("patch", "get")
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_admin:
            return User.objects.all()
        return User.objects.exclude(is_admin=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj
