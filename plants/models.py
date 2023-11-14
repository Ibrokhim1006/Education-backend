from django.db import models
from authen.models import (
    CustomUser
)


class PlantCategories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Plants(models.Model):
    plant_name = models.CharField(max_length=255, null=True, blank=True)
    plant_temperature = models.CharField(max_length=255, null=True, blank=True)
    plant_water = models.CharField(max_length=255, null=True, blank=True)
    plant_light = models.CharField(max_length=255, null=True, blank=True)
    plant_tall = models.CharField(max_length=255, null=True, blank=True)
    plant_price = models.CharField(max_length=255, null=True, blank=True)
    plant_description = models.CharField(max_length=255, null=True, blank=True)
    plant_categories = models.ForeignKey(
        PlantCategories, on_delete=models.CASCADE, null=True, blank=True
    )
    plant_type = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


class PlantImages(models.Model):
    plant_id = models.ForeignKey(
        Plants,
        on_delete=models.CASCADE, null=True, blank=True, related_name="img"
    )
    plant_image = models.ImageField(upload_to="plants/", null=True, blank=True)

    def __str__(self):
        return self.plant_id.plant_name


class CarePlanting(models.Model):
    care_plant_name = models.CharField(max_length=255, null=True, blank=True)
    care_plant_video = models.FileField(
        upload_to="videos/", null=True, blank=True)
    care_plant_video_minutes = models.CharField(
        max_length=255, null=True, blank=True)
    care_plant_desc = models.TextField(null=True, blank=True)
    care_plant_content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.care_plant_name


class CareTopics(models.Model):
    care_plant_id = models.ForeignKey(
        CarePlanting, on_delete=models.CASCADE, null=True, blank=True
    )
    care_topic_name = models.CharField(max_length=255, null=True, blank=True)
    care_topic_video = models.FileField(
        upload_to="videos/", null=True, blank=True)
    care_topic_video_minutes = models.CharField(
        max_length=255, null=True, blank=True)
    care_topic_view_user = models.ManyToManyField(
        CustomUser,
        null=True, blank=True
    )


    def __str__(self):
        return self.care_topic_name


class CareTopicHistory(models.Model):
    care_topic_id = models.ForeignKey(
        CareTopics, on_delete=models.CASCADE,
        null=True, blank=True
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.care_topic_id.care_topic_name} {self.user.first_name} {self.user.last_name}'


class LocationPlantMarket(models.Model):
    location_name = models.CharField(max_length=255, null=True, blank=True)
    location_img = models.ImageField(upload_to='shops/', null=True, blank=True)
    location_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.location_name


class CarePlantingTree(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to='shops/', null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
