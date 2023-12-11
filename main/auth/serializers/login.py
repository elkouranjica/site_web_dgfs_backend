from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from rest_framework import serializers

from main.user.models import User
from main.user.serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        matricule = attrs['matricule']
        password = attrs['password']
        try:
            user = User.objects.get(matricule=matricule)
        except User.DoesNotExist:
            raise serializers.ValidationError({"warning": "Le matricule n'existe pas"})

        if not user.check_password(password):
            raise serializers.ValidationError({"warning": "Le mot de passe est éronné"})

        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["user"] = UserSerializer(self.user, context=self.context).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
