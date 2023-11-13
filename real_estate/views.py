""" Django DRF Packaging """
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authen.renderers import UserRenderers
from real_estate.models import (
    Currency,
    Region,
    Distric,
    CategoriesRealEstet,
    AdType,
    AdSubCategory,
    Repair,
    BuildMaterial,
    Price,
    Amenities,
    NumberRooms,
    RealEstate,
    RealEstetImgaes,
    BuyRealEstet,
)
from real_estate.serializers import (
    CurrencySerializers,
    RegionSerializers,
    DistricSerializers,
    CategoriesRealEstetSerializers,
    AdTypeSerializers,
    AdTypeCrudSerializers,
    AdSubCategorySerializers,
    AdSubCategoryCrudSerializers,
    RepairtSerializers,
    BuildMaterialSerializers,
    BuildMaterialCrudSerializers,
    PriceSerializers,
    AmenitiesSerializers,
    AmenitiesCrudSerializers,
    NumberRoomsSerializers,
    RealEstetImgaessSerializers,
    RealEstateSerializers,
    RealEstateCrudSerializers,
    RealEstetImgaesSerializers,
    BuyRealEstetSerializers,
    SendBuyRealEstetSerializers,
)


class RegionsListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = Region.objects.all()
        serializers = RegionSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class DistricListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Distric.objects.filter(region_id=pk)
        serializers = DistricSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CurrencyListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = Currency.objects.all()
        serializers = CurrencySerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CategoriesRealEstetListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = CategoriesRealEstet.objects.all()
        serializers = CategoriesRealEstetSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# ad type
class AdTypeListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = AdType.objects.all()
        serializers = AdTypeSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ ad type POST views """
        serializer = AdTypeCrudSerializers(
            data=request.data,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdTypeCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = AdType.objects.filter(id=pk)
        serializers = AdTypeSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = AdTypeCrudSerializers(
            instance=AdType.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = AdType.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


# Ad subcategory
class AdSubCategoryListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = AdSubCategory.objects.all()
        serializers = AdSubCategorySerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ AdSubCategory POST views """
        serializer = AdSubCategoryCrudSerializers(
            data=request.data,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdSubCategoryCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = AdSubCategory.objects.filter(id=pk)
        serializers = AdSubCategorySerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = AdSubCategoryCrudSerializers(
            instance=AdSubCategory.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = AdSubCategory.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class RepairListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = Repair.objects.all()
        serializers = RepairtSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# Build material
class BuildMaterialListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = BuildMaterial.objects.all()
        serializers = BuildMaterialSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = BuildMaterialCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BuildMaterialCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = BuildMaterial.objects.filter(id=pk)
        serializers = BuildMaterialSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = BuildMaterialCrudSerializers(
            instance=BuildMaterial.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = BuildMaterial.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class PriceListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = Price.objects.all()
        serializers = PriceSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# Ammenties
class AmenitiesListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = Amenities.objects.all()
        serializers = AmenitiesSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = AmenitiesCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AmenitiesCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Amenities.objects.filter(id=pk)
        serializers = AmenitiesSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = AmenitiesCrudSerializers(
            instance=Amenities.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = Amenities.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class NumberRoomsListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = NumberRooms.objects.all()
        serializers = NumberRoomsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# Real estet
class RealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = RealEstate.objects.all()
        serializers = RealEstateSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        """RealEstateListViews POST views"""
        serializer = RealEstateCrudSerializers(
            data=request.data,
            context={
                "author_id": request.user,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


class RealEstateCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = RealEstate.objects.filter(id=pk)
        serializers = RealEstateSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = RealEstateCrudSerializers(
            instance=RealEstate.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = RealEstate.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class RealEstateImgViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = RealEstetImgaes.objects.filter(id=pk)
        serializers = RealEstetImgaessSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = RealEstetImgaesSerializers(
            instance=RealEstetImgaes.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(img=request.data.get("img"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = RealEstetImgaes.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class MyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = RealEstate.objects.filter(
            author_id=request.user.id)
        serializers = RealEstateSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class BuyMyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = RealEstate.objects.filter(
            author_id=request.user.id, is_active=True)
        serializers = RealEstateSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ActiveMyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = RealEstate.objects.filter(
            author_id=request.user.id, is_active=False)
        serializers = RealEstateSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class SenByuyMyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = BuyRealEstet.objects.filter(
            real_estet_id__author_id=request.user.id, is_active=False)
        serializers = BuyRealEstetSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request):
        objects_list = BuyRealEstet.objects.filter(
            real_estet_id__author_id=request.user.id, is_active=False)[0]
        objects_list.is_active = True
        objects_list.save()
        return Response({'message': 'save'}, status=status.HTTP_200_OK)


class UserBuyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        objects_list = BuyRealEstet.objects.filter(
            user_id=request.user.id, is_active=True)
        serializers = BuyRealEstetSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UserSendBuyRealEstateListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = BuyRealEstet.objects.filter(
            id=pk,
            user_id=request.user.id, is_active=True)
        serializers = BuyRealEstetSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        real_estate = RealEstate.objects.filter(id=pk)[0]
        """RealEstateListViews POST views"""
        serializer = SendBuyRealEstetSerializers(
            data=request.data,
            context={
                "user_id": request.user,
                "real_estet_id": real_estate,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
