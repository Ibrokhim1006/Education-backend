""" Django Rest Framework Library """
from rest_framework import serializers

""" Authentification Serializer """
from authen.serializers import (
    UserInformationSerializers
)
from youtobe.models import (
    Explore,
)


class ExploreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Explore
        fields = ['explore', 'id']