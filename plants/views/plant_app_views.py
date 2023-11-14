""" Django Library """
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

""" Django Rest Framework Library """
from rest_framework import generics, permissions, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import filters

from plants.serializers.plant_app_serializers import (
    PlantCategoriesSerializer,
    PlantsSerializer,
    CarePlantingSerializer,
    CareTopicSerializer,
    PlantTopicHistorySeriazlier,
)
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



class PlantCategoriesView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = PlantCategories.objects.all()
        serializer = PlantCategoriesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantRecentlyViewedView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Plants.objects.all()[0:4]
        serializer = PlantsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantPopularView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Plants.objects.all().order_by("-id")[0:4]
        serializer = PlantsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantFilterCategoriesView(APIView):
    def get(self, request, id, *args, **kwargs):
        filter_by = get_object_or_404(PlantCategories, id=id)
        queryset = Plants.objects.select_related('plant_categories').filter(
            plant_categories=filter_by
        ).order_by("-id")[0:4]
        serializer = PlantsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantGetView(APIView):

    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(Plants, id=id)
        serializer = PlantsSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarePlantingView(APIView):

    def get(self, request, *args, **kwargs):

        return
