from django.contrib import admin

from plants.models import (
    PlantCategories,
    Plants,
    PlantImages,
    CarePlanting,
    CareTopics,
    CareTopicHistory,
    LocationPlantMarket,
    CarePlantingTree,
    PlantRecentlyViewed
)


admin.site.register(PlantCategories)
admin.site.register(Plants)
admin.site.register(PlantImages)
admin.site.register(CarePlanting)
admin.site.register(CareTopics)
admin.site.register(CareTopicHistory)
admin.site.register(LocationPlantMarket)
admin.site.register(CarePlantingTree)
admin.site.register(PlantRecentlyViewed)
