from rest_framework import routers

from main.auth.viewsets.logout import LogoutViewSet
from main.etablissement.viewsets.etablissement import EtablissementViewSet
from main.message.viewsets import MessageViewSet
from main.partenaire.viewsets import PartenaireViewSet
from main.post.viewsets import PostViewSet
from main.user.viewsets import UserViewSet
from main.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from main.institution.viewsets import MinistereViewSet, DirectionViewSet, ServiceViewSet,\
    DirecteurViewSet, ChefServiceViewSet


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


# ##################################################################### #
# ################### INSTITUTIONS               ###################### #
# ##################################################################### #
router.register(r"ministere", MinistereViewSet, basename="ministere")
router.register(r"direction", DirectionViewSet, basename="direction")
router.register(r"service", ServiceViewSet, basename="service")
router.register(r"directeur", DirecteurViewSet, basename="directeur")
router.register(r"chef-service", ChefServiceViewSet, basename="chef-service")


# ##################################################################### #
# ################### PARTENAIRES                   ###################### #
# ##################################################################### #
router.register(r"partenaires", PartenaireViewSet, basename="partenaire")


urlpatterns = [*router.urls]
