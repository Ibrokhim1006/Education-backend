""" DJango DRF Serializers """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from authen.models import CustomUser


class UserGroupsSerializers(serializers.ModelSerializer):
    """Groups User Serializers"""

    class Meta:
        """Groups User Fields"""

        model = Group
        fields = ("id", "name")


class UserInformationSerializers(serializers.ModelSerializer):
    """User Profiles Serializers"""

    groups = UserGroupsSerializers(read_only=True, many=True)

    class Meta:
        """User Model Fileds"""

        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "groups"]
