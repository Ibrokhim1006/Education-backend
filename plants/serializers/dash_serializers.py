from rest_framework import serializers
from plants.models import (
    PlantCategories,
)


class PlantCategoriesSerializers(serializers.ModelSerializer):
    """Plant Categoriyes Serializers"""

    class Meta:
        """Plant Categoriyes Model Fileds"""

        model = PlantCategories
        fields = ["id", "name"]


class PlantCategoriesCrudSerializers(serializers.ModelSerializer):
    """Plant Categoriyes Serializers"""

    class Meta:
        """Plant Categoriyes Model Fileds"""

        model = PlantCategories
        fields = ["id", "name"]

    def create(self, validated_data):
        """PlantCategories Create Function"""
        return PlantCategories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """PlantCategories Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
