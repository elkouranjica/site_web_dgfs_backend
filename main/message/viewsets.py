from main.abstract.viewsets import AbstractViewSet
from main.message.models import Message
from main.message.serializers import MessageSerializer
from rest_framework.permissions import AllowAny


class MessageViewSet(AbstractViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)
    http_method_names = "get"

    def get_object(self):
        obj = Message.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
