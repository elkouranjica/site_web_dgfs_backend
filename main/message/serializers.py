from main.abstract.serializers import AbstractSerializer
from main.message.models import Message


class MessageSerializer(AbstractSerializer):
    class Meta:
        model = Message
        fields = '__all__'
