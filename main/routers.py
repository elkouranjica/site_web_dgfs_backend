from rest_framework import routers

from main.auth.viewsets.logout import LogoutViewSet
from main.etablissement.viewsets.etablissement import EtablissementViewSet
from main.message.viewsets import MessageViewSet
from main.post.viewsets import PostViewSet
from main.user.viewsets import UserViewSet
from main.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet


router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")


# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #
router.register(r"user", UserViewSet, basename="user")


# ##################################################################### #
# ################### ETABLISSEMENT              ###################### #
# ##################################################################### #
router.register(r"etablissement", EtablissementViewSet, basename="etablissement")


# ##################################################################### #
# ################### ACTUALITÉS                 ###################### #
# ##################################################################### #
router.register(r"post", PostViewSet, basename="post")


# ##################################################################### #
# ################### MESSAGES                   ###################### #
# ##################################################################### #
router.register(r"message", MessageViewSet, basename="message")

urlpatterns = [*router.urls]
