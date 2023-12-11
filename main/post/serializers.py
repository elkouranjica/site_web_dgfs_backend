from main.abstract.serializers import AbstractSerializer
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth import get_user_model
from main.post.models import Post


class AuthorSerializer(AbstractSerializer):
    class Meta:
        model = get_user_model()
        fields = ["last_name", "first_name"]


class PostSerializer(AbstractSerializer, TaggitSerializer):
    tags = TagListSerializerField()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = "__all__"
