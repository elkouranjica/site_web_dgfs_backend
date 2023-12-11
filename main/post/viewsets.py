from rest_framework.permissions import AllowAny

from main.abstract.viewsets import AbstractViewSet
from main.post.models import Post
from main.post.serializers import PostSerializer


class PostViewSet(AbstractViewSet):
    http_method_names = "get"
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.published.all()

    def get_object(self):
        obj = Post.published.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
