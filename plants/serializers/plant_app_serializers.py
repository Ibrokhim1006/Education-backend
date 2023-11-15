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
    LocationPlantMarket,
    CarePlantingTree,
    PlantRecentlyViewed,
)

from authen.serializers import (
    UserInformationSerializers
)
from plants.serializers.dash_serializers import PlantSerializers



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
            'care_plant_desc',
            'care_plant_content'
        ]


class CareTopicSerializer(serializers.ModelSerializer):
    care_plant_id = CarePlantingSerializer(read_only=True)
    care_topic_view_user = UserInformationSerializers(read_only=True, many=True)

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


class PlantTopicHistoryCreateSeriazlier(serializers.ModelSerializer):

    class Meta:
        model = CareTopicHistory
        fields = [
            'id',
            'care_topic_id',
            'user',
            'created_at',
        ]
        def create(self, validated_data):
            create = CareTopicHistory.objects.create(
                **validated_data
            )
            create.user = self.context.get('user')
            create.save()
            return create


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationPlantMarket
        fields = [
            'id',
            'location_name',
            'location_img',
            'location_url'
        ]


class CarePlantingTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarePlantingTree
        fields = [
            'id',
            'name',
            'img',
            'price',
            'description',
        ]


class PlantRecentlyViewedSerializer(serializers.ModelSerializer):
    plant_id = PlantSerializers(read_only=True)
    user = UserInformationSerializers(read_only=True)

    class Meta:
        model = PlantRecentlyViewed
        fields = [
            'plant_id',
            'user',
            'created_at'
        ]

        def create(self, validated_data):
            create = PlantRecentlyViewed.objects.create(
                **validated_data
            )
            create.user = self.context.get('user')
            create.save()
            return create