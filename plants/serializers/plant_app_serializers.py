""" Django Rest Framework Library """
from rest_framework import serializers

""" Plant Model """
from plants.models import (
    PlantCategories,
    Plants,
    PlantImages,
    CarePlanting,
    CareTopics,
    CareTopicHistory,
    LocationPlantMarket
)

from authen.serializers import (
    UserInformationSerializers
)




class PlantCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantCategories
        fields = [
            'id',
            'name'
        ]


class PlantsSerializer(serializers.ModelSerializer):
    plant_categories = PlantCategoriesSerializer(read_only=True)

    class Meta:
        model = Plants
        fields = [
            'id',
            'plant_name',
            'plant_temperature',
            'plant_water',
            'plant_light',
            'plant_tall',
            'plant_price',
            'plant_description',
            'plant_categories',
            'plant_type',
        ]


class CarePlantingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarePlanting
        fields = [
            'id',
            'care_plant_name',
            'care_plant_video',
            'care_plant_video_minutes',
        ]


class CareTopicSerializer(serializers.ModelSerializer):
    care_plant_id = CarePlantingSerializer(read_only=True)
    care_view_user = UserInformationSerializers(read_only=True, many=True)

    class Meta:
        model = CareTopics
        fields = [
            'id',
            'care_plant_id',
            'care_topic_name',
            'care_topic_video',
            'care_topic_video_minutes',
            'care_topic_view_user'
        ]


class PlantTopicHistorySeriazlier(serializers.ModelSerializer):
    care_topic_id = CareTopicSerializer(read_only=True)
    user = UserInformationSerializers(read_only=True)

    class Meta:
        model = CareTopicHistory
        fields = [
            'id',
            'care_topic_id',
            'user',
            'created_at',
        ]