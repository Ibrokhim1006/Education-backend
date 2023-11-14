from django.urls import path
from plants.views.dash_views import (
    PlantsCategroiresViews,
    PlantsCategroiresCrudViews,
    PlantsViews,
    PlantsCrudViews,
    PlantsImgCrudViews,

)

from plants.views.plant_app_views import (
    PlantCategoriesView,
    PlantRecentlyViewedView,
    PlantPopularView,
    PlantFilterCategoriesView,
    PlantGetView
)

urlpatterns = [
    # plants app
    path('app/plant-categories/', PlantCategoriesView.as_view(), name='plant-categories'),
    path('app/plant-recently-viewed/', PlantRecentlyViewedView.as_view(), name='plant-recently-viewed'),
    path('app/plant-popular/', PlantPopularView.as_view(), name='plant-popular'),
    path('app/plant-filter-categories/<int:id>/', PlantFilterCategoriesView.as_view(), name='plant-filter-categories'),
    path('app/plant-profile/', PlantGetView.as_view(), name='plat-profile')
]
