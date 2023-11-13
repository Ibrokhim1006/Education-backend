from django.urls import path
from real_estate.views import (
    RegionsListViews,
    DistricListViews,
    CurrencyListViews,
    CategoriesRealEstetListViews,
    AdTypeListViews,
    AdTypeCrudViews,
    AdSubCategoryListViews,
    RepairListViews,
    BuildMaterialListViews,
    PriceListViews,
    AmenitiesListViews,
    NumberRoomsListViews,
    RealEstateListViews,
    MyRealEstateListViews,
    BuyMyRealEstateListViews,
    ActiveMyRealEstateListViews,
    SenByuyMyRealEstateListViews,
    UserBuyRealEstateListViews,
    UserSendBuyRealEstateListViews,
)

urlpatterns = [
    path("regions_list_views/", RegionsListViews.as_view()),
    path("distric_list_views/<int:pk>/", DistricListViews.as_view()),
    path("currency_list_views/", CurrencyListViews.as_view()),
    path(
        "categories_real_estet_list_views/",
        CategoriesRealEstetListViews.as_view()),
    path("adtype_list_views/", AdTypeListViews.as_view()),
    path('adtype_crud_views/<int:pk>/', AdTypeCrudViews.as_view()),
    path("adsub_category_list_views/", AdSubCategoryListViews.as_view()),
    path("repair_list_views/", RepairListViews.as_view()),
    path("build_material_list_views/", BuildMaterialListViews.as_view()),
    path("price_list_views/", PriceListViews.as_view()),
    path("amenities_list_views/", AmenitiesListViews.as_view()),
    path("number_rooms_list_views/", NumberRoomsListViews.as_view()),
    path("real_estate_list_views/", RealEstateListViews.as_view()),
    path('my_real_estate_list_views/', MyRealEstateListViews.as_view()),
    path('buy_myreal_estate_list_views/', BuyMyRealEstateListViews.as_view()),
    path(
        'active_myreal_estate_list_views/',
        ActiveMyRealEstateListViews.as_view()),
    path(
        'send_buy_myreal_estate_list_views/',
        SenByuyMyRealEstateListViews.as_view()),
    path(
        'user_buy_real_estate_list_views/',
        UserBuyRealEstateListViews.as_view()),
    path(
        'user_send_buy_real_estate_list_views/<int:pk>/',
        UserSendBuyRealEstateListViews.as_view()),
]
