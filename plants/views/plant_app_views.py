""" Django Library """
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, F

""" Django Rest Framework Library """
from rest_framework import generics, permissions, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import filters
from datetime import datetime, timedelta

from plants.serializers.plant_app_serializers import (
    PlantCategoriesSerializer,
    PlantsSerializer,
    CarePlantingSerializer,
    CareTopicSerializer,
    PlantTopicHistorySeriazlier,
    PlantTopicHistoryCreateSeriazlier,
    LocationSerializer,
    CarePlantingTreeSerializer,
    PlantRecentlyViewedSerializer
)

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
    PlantRecentlyViewed
)
from authen.renderers import UserRenderers

from plants.serializers.dash_serializers import PlantSerializers


class PlantCategoriesView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = PlantCategories.objects.all()
        serializer = PlantCategoriesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantRecentlyViewedView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Plants.objects.all()[0:4]
        serializer = PlantSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantPopularView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Plants.objects.all().order_by("-id")[0:4]
        serializer = PlantSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantFilterCategoriesView(APIView):
    def get(self, request, id, *args, **kwargs):
        filter_by = get_object_or_404(PlantCategories, id=id)
        queryset = (
            Plants.objects.select_related("plant_categories")
            .filter(plant_categories=filter_by)
            .order_by("-id")[0:4]
        )
        serializer = PlantSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlantGetView(APIView):
    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(Plants, id=id)
        serializer = PlantSerializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarePlantingView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = CarePlanting.objects.all()
        serializer = CarePlantingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarePlantingGetView(APIView):

    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(CarePlanting, id=id)
        serializer = CarePlantingSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CareTopicsView(APIView):
    def get(self, request, id, *args, **kwargs):
        filter_by = get_object_or_404(CarePlanting, id=id)
        queryset = CareTopics.objects.select_related("care_plant_id").filter(
            Q(care_plant_id=filter_by)
        )
        serializer = CareTopicSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CareTopicGetView(APIView):

    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(CareTopics, id=id)
        serializer = CareTopicSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CareTopicsHistoryView(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [permissions.IsAuthenticatedOrReadOnly, AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = CareTopicHistory.objects.select_related("user").filter(
            Q(user=request.user)
        )
        serializer = PlantTopicHistorySeriazlier(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PlantTopicHistoryCreateSeriazlier(
            data=request.data, partial=True, context={"user": request.user}
        )
        if serializer.save(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationMarketView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = LocationPlantMarket.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarePlantingTreeView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = CarePlantingTree.objects.all()
        serializer = CarePlantingTreeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class LastRecentlyViewedPlantView(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [permissions.IsAuthenticatedOrReadOnly, AllowAny]

    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        delta = timedelta(days=7)
        start_date = today - delta
        end_date = today + delta
        queryset = PlantRecentlyViewed.objects.select_related('user').filter(
            Q(user=request.user)
        ).filter(
            Q(created_at__range=(start_date, end_date))
        ).order_by(F('created_at').desc())
        serializer = PlantRecentlyViewedSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecentlyUploadedView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        delta = timedelta(days=7)
        start_date = today - delta
        end_date = today + delta

        queryset = CareTopics.objects.filter(
            Q(created_at__range=(start_date, end_date))
        )
        serializer = CareTopicSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = PlantRecentlyViewedSerializer(
            data=request.data,
            partial=True,
            context={
                'user': request.user
            }
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class PlantSearchView(generics.ListAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['plant_name']


class CarePlantingSearchView(generics.ListAPIView):
    queryset = CarePlanting.objects.all()
    serializer_class = CarePlantingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['care_plant_name']


class CarePlantingTreeSearchView(generics.ListAPIView):
    queryset = CarePlantingTree.objects.all()
    serializer_class = CarePlantingTreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
