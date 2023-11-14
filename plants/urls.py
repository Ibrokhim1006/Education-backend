from django.urls import path
from plants.views.dash_views import (
    PlantsCategroiresViews,
    PlantsCategroiresCrudViews,
    PlantsViews,
    PlantsCrudViews,
    PlantsImgCrudViews,

)

urlpatterns = [
    path('dash/plants_categroires_views/', PlantsCategroiresViews.as_view()),
    path(
        'dash/plants_categroires_crud_views/<int:pk>/',
        PlantsCategroiresCrudViews.as_view()),
    path('dash/plants_views/', PlantsViews.as_view()),
    path('dash/plants_crud_views/<int:pk>/', PlantsCrudViews.as_view()),
    path('dash/plants_img_crud_views/<int:pk>/', PlantsImgCrudViews.as_view()),

]
