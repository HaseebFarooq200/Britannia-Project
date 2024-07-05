from rest_framework import serializers
from system_user.models.custom_user import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "UserID",
            "Email",
            "UserName",
            "PhoneNumber",
            "password",
            "IsAdmin",
            "CreatedAt",
            "UpdatedAt",
        ]
        extra_kwargs = {
            "UserID": {"read_only": True},
            "CreatedAt": {"read_only": True},
            "UpdatedAt": {"read_only": True},
            "password": {"write_only": True},
        }

    def save(self):
        user = CustomUser(
            Email=self.validated_data["Email"],
            UserName=self.validated_data["UserName"],
            PhoneNumber=self.validated_data["PhoneNumber"],
            IsAdmin=self.validated_data["IsAdmin"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user
