from django.urls import path
from plants.views.dash_views import (
    PlantsCategroiresViews,
    PlantsCategroiresCrudViews,
    PlantsViews,
    PlantsCrudViews,
    PlantsImgCrudViews,
    CarePlantingViews,
    CarePlantingCrudViews,
    CareTopicsViews,
    CareTopicsCrudViews,
    LocationPlantMarketViews,
    LocationPlantMarketCrudViews,
    CareTopicHistoryViews,
)
from plants.views.plant_app_views import (
    PlantCategoriesView,
    PlantRecentlyViewedView,
    PlantPopularView,
    PlantFilterCategoriesView,
    PlantGetView,
    CarePlantingView,
    CareTopicsView,
    CareTopicsHistoryView,
    LocationMarketView,
    CarePlantingTreeView,
    CarePlantingGetView
)

urlpatterns = [
    path("dash/plants_categroires_views/", PlantsCategroiresViews.as_view()),
    path(
        "dash/plants_categroires_crud_views/<int:pk>/",
        PlantsCategroiresCrudViews.as_view(),
    ),
    path("dash/plants_views/", PlantsViews.as_view()),
    path("dash/plants_crud_views/<int:pk>/", PlantsCrudViews.as_view()),
    path("dash/plants_img_crud_views/<int:pk>/", PlantsImgCrudViews.as_view()),
    path('dash/care_planting_views/', CarePlantingViews.as_view()),
    path(
        'dash/care_planting_crud_views/<int:pk>/',
        CarePlantingCrudViews.as_view()),
    path('dash/care_topics_views/', CareTopicsViews.as_view()),
    path(
        'dash/care_topics_crud_views/<int:pk>/',
        CareTopicsCrudViews.as_view()),
    path(
        'dash/location_plant_market_views/',
        LocationPlantMarketViews.as_view()),
    path(
        'dash/location_plant_market_crud_views/<int:pk>/',
        LocationPlantMarketCrudViews.as_view()),
    path('dash/care_topic_history_views/', CareTopicHistoryViews.as_view()),
    # plants app
    path(
        "app/plant-categories/",
        PlantCategoriesView.as_view(), name="plant-categories"
    ),
    path(
        "app/plant-recently-viewed/",
        PlantRecentlyViewedView.as_view(),
        name="plant-recently-viewed",
    ),
    path(
        "app/plant-popular/",
        PlantPopularView.as_view(), name="plant-popular"),
    path(
        "app/plant-filter-categories/<int:id>/",
        PlantFilterCategoriesView.as_view(),
        name="plant-filter-categories",
    ),
    path("app/plant-profile/", PlantGetView.as_view(), name="plat-profile"),
    path('app/plant-categories/', PlantCategoriesView.as_view(), name='plant-categories'),
    path('app/plant-recently-viewed/', PlantRecentlyViewedView.as_view(), name='plant-recently-viewed'),
    path('app/plant-popular/', PlantPopularView.as_view(), name='plant-popular'),
    path('app/plant-filter-categories/<int:id>/', PlantFilterCategoriesView.as_view(), name='plant-filter-categories'),
    path('app/plant-profile/', PlantGetView.as_view(), name='plant-profile'),
    path('app/plant-care/', CarePlantingView.as_view(), name='plant-care'),
    path('app/plant-care/<int:id>/', CarePlantingGetView.as_view(), name='plant-care'),
    path('app/plant-care-topic/<int:id>/', CareTopicsView.as_view(), name='plant-care-topic'),
    path('app/plant-care-topic-history/', CareTopicsHistoryView.as_view(), name='plant-care-topic-history'),
    path('app/plant-location-market/', LocationMarketView.as_view(), name='plant-location-market'),
    path('app/plant-care-trees/', CarePlantingTreeView.as_view(), name='plant-care-trees'),
]
