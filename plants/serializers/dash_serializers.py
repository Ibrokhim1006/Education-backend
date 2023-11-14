from rest_framework import serializers
from plants.models import (
    PlantCategories,
    Plants,
    PlantImages,
    CarePlanting,
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


# Plants
class PlantImagesSerializers(serializers.ModelSerializer):
    """PlantImages Serializers"""

    class Meta:
        """PlantImages Model Fileds"""

        model = PlantImages
        fields = ["id", "plant_id", "plant_image"]


class PlantSerializers(serializers.ModelSerializer):
    """Plants Serializers"""

    plant_categories = PlantCategoriesSerializers(read_only=True)
    img = PlantImagesSerializers(many=True, read_only=True)

    class Meta:
        """Plants Model Fileds"""

        model = Plants
        fields = [
            "id",
            "plant_name",
            "plant_temperature",
            "plant_water",
            "plant_light",
            "plant_tall",
            "plant_categories",
            "plant_type",
            "img",
            "created_at",
        ]


class PlantCrudSerializers(serializers.ModelSerializer):
    """Plants Serializers"""

    plant_image = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        """Plants Model Fileds"""

        model = Plants
        fields = [
            "id",
            "plant_name",
            "plant_temperature",
            "plant_water",
            "plant_light",
            "plant_tall",
            "plant_categories",
            "plant_type",
            "created_at",
        ]

    def create(self, validated_data):
        """Plants Create And Multiple Img Funcation"""
        plant_image = validated_data.pop("plant_image")
        plant_img = Plants.objects.create(**validated_data)
        for item in plant_image:
            images = PlantImages.objects.create(
                plant_id=plant_img, plant_image=item)
            images.save()
        return plant_img

    def update(self, instance, validated_data):
        """Plants Update Funcation"""
        instance.plant_name = validated_data.get(
            "plant_name", instance.plant_name)

        instance.plant_temperature = validated_data.get(
            "plant_temperature", instance.plant_temperature
        )

        instance.plant_water = validated_data.get(
            "plant_water", instance.plant_water)

        instance.plant_light = validated_data.get(
            "plant_light", instance.plant_light)

        instance.plant_tall = validated_data.get(
            "plant_tall", instance.plant_tall)

        instance.plant_categories = validated_data.get(
            "plant_categories", instance.plant_categories
        )

        instance.plant_type = validated_data.get(
            "plant_type", instance.plant_type)
        instance.save()
        return instance


class PlantImagesCrudSerializers(serializers.ModelSerializer):
    """PlantImages Serializers"""
    plant_image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        """PlantImages Model Fileds"""

        model = PlantImages
        fields = ["id", "plant_id", "plant_image"]

    def update(self, instance, validated_data):
        """RealEstate Update Funcation"""
        if instance.plant_image == None:
            instance.plant_image = self.context.get("plant_image")
        else:
            instance.plant_image = validated_data.get(
                    "plant_image", instance.plant_image)
        instance.save()
        return instance


# Care plating
class CarePlantingSerializers(serializers.ModelSerializer):
    """CarePlanting Serializers"""

    class Meta:
        """CarePlanting Model Fileds"""

        model = CarePlanting
        fields = [
            "id",
            "care_plant_name",
            "care_plant_video",
            "care_plant_video_minutes",
        ]


class CarePlantingCrudSerializers(serializers.ModelSerializer):
    """CarePlanting Serializers"""

    care_plant_video = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        """CarePlanting Model Fileds"""

        model = CarePlanting
        fields = [
            "id",
            "care_plant_name",
            "care_plant_video",
            "care_plant_video_minutes",
        ]

    def create(self, validated_data):
        """CarePlanting Create And Multiple Img Funcation"""
        care_plating = CarePlanting.objects.create(**validated_data)
        care_plating.save()
        return care_plating

    def update(self, instance, validated_data):
        """CarePlanting Update Funcation"""
        instance.care_plant_name = validated_data.get(
            "care_plant_name", instance.care_plant_name)

        instance.care_plant_video_minutes = validated_data.get(
            "care_plant_video_minutes", instance.care_plant_video_minutes
        )

        if instance.care_plant_video == None:
            instance.care_plant_video = self.context.get("care_plant_video")
        else:
            instance.care_plant_video = validated_data.get(
                "care_plant_video", instance.care_plant_video)
        instance.save()
        return instance
