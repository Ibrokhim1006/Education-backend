""" DJango DRF Serializers """
from rest_framework import serializers
from authen.models import CustomUser, PyemntSumm
from real_estate.models import (
    Currency,
    Region,
    Status,
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


class PyemntSummSerializers(serializers.ModelSerializer):
    """PyemntSumm Serializers"""

    class Meta:
        """PyemntSumm Model Fileds"""

        model = PyemntSumm
        fields = "__all__"


class UserInformationSerializers(serializers.ModelSerializer):
    """User Profiles Serializers"""

    class Meta:
        """User Model Fileds"""

        model = CustomUser
        fields = ["id", "first_name", "last_name", "email"]


class CurrencySerializers(serializers.ModelSerializer):
    """Currency Serializer"""

    class Meta:
        model = Currency
        fields = "__all__"


class RegionSerializers(serializers.ModelSerializer):
    """Region Serializer"""

    class Meta:
        model = Region
        fields = "__all__"


class DistricSerializers(serializers.ModelSerializer):
    """Distric Serializer"""

    region_id = RegionSerializers(read_only=True)

    class Meta:
        model = Distric
        fields = "__all__"


class StatusSerializers(serializers.ModelSerializer):
    """Status Serializer"""

    class Meta:
        model = Status
        fields = "__all__"


class CategoriesRealEstetSerializers(serializers.ModelSerializer):
    """CategoriesRealEstet Serializer"""

    class Meta:
        model = CategoriesRealEstet
        fields = "__all__"


class AdTypeSerializers(serializers.ModelSerializer):
    """AdType Serializer"""

    id_category = CategoriesRealEstetSerializers(read_only=True)

    class Meta:
        model = AdType
        fields = "__all__"


# ad Type Categories
class AdTypeCrudSerializers(serializers.ModelSerializer):
    """AdType Serializer"""

    class Meta:
        model = AdType
        fields = ["id", "name", "id_category"]

    def create(self, validated_data):
        """AdType Create Function"""
        return AdType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """AdType Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.id_category = validated_data.get(
            "id_category", instance.id_category)
        instance.save()
        return instance


# ad SubCategories
class AdSubCategorySerializers(serializers.ModelSerializer):
    """AdSubCategory Serializer"""

    id_ad_type = AdTypeSerializers(read_only=True)

    class Meta:
        model = AdSubCategory
        fields = "__all__"


class AdSubCategoryCrudSerializers(serializers.ModelSerializer):
    """AdSubCategory Serializer"""

    class Meta:
        model = AdSubCategory
        fields = ["id", "name", "id_ad_type"]

    def create(self, validated_data):
        """AdSubCategory Create Function"""
        return AdSubCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """AdSubCategory Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.id_ad_type = validated_data.get(
            "id_ad_type", instance.id_ad_type)
        instance.save()
        return instance


class RepairtSerializers(serializers.ModelSerializer):
    """Repair Serializer"""

    class Meta:
        model = Repair
        fields = "__all__"


# Build Material
class BuildMaterialSerializers(serializers.ModelSerializer):
    """BuildMaterial Serializer"""

    class Meta:
        model = BuildMaterial
        fields = "__all__"


class BuildMaterialCrudSerializers(serializers.ModelSerializer):
    """BuildMaterial Serializer"""

    class Meta:
        model = BuildMaterial
        fields = ["id", "name"]

    def create(self, validated_data):
        """BuildMaterial Create Function"""
        return BuildMaterial.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """BuildMaterial Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class PriceSerializers(serializers.ModelSerializer):
    """Price Serializer"""

    class Meta:
        model = Price
        fields = "__all__"


# Amenities
class AmenitiesSerializers(serializers.ModelSerializer):
    """Amenities Serializer"""

    class Meta:
        model = Amenities
        fields = "__all__"


class AmenitiesCrudSerializers(serializers.ModelSerializer):
    """Amenities Serializer"""

    class Meta:
        model = Amenities
        fields = ["id", "name"]

    def create(self, validated_data):
        """Amenities Create Function"""
        return Amenities.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Amenities Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class NumberRoomsSerializers(serializers.ModelSerializer):
    """NumberRooms Serializer"""

    class Meta:
        model = NumberRooms
        fields = "__all__"


# Real Estet
class RealEstetImgaessSerializers(serializers.ModelSerializer):
    """RealEstetImgaes Serializer"""

    class Meta:
        model = RealEstetImgaes
        fields = "__all__"


class RealEstateSerializers(serializers.ModelSerializer):
    """RealEstate Serializer"""

    category_id = CategoriesRealEstetSerializers(read_only=True)
    ad_taype_id = AdTypeSerializers(read_only=True)
    ad_subcategory_id = AdSubCategorySerializers(read_only=True)
    repair_id = RepairtSerializers(read_only=True)
    build_mateial_id = BuildMaterialSerializers(read_only=True)
    price_id = PriceSerializers(read_only=True)
    amenities_id = AmenitiesSerializers(many=True, read_only=True)
    number_romm_id = NumberRoomsSerializers(read_only=True)
    currency_id = CurrencySerializers(read_only=True)
    author_id = UserInformationSerializers(read_only=True)
    img = RealEstetImgaessSerializers(many=True, read_only=True)
    payment_id = PyemntSummSerializers(read_only=True)

    class Meta:
        model = RealEstate
        fields = [
            "id",
            "category_id",
            "ad_taype_id",
            "ad_subcategory_id",
            "repair_id",
            "build_mateial_id",
            "price_id",
            "amenities_id",
            "number_romm_id",
            "currency_id",
            "is_appropriate",
            "author_id",
            "distric_id",
            "status_id",
            "payment_id",
            "is_payment",
            "apartment_area",
            "house_area",
            "floors_building",
            "price",
            "content",
            "is_active",
            "img",
            "datetime",
        ]


class RealEstateCrudSerializers(serializers.ModelSerializer):
    """RealEstate Serializer"""
    img = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000,
            allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = RealEstate
        fields = [
            "id",
            "category_id",
            "ad_taype_id",
            "ad_subcategory_id",
            "repair_id",
            "build_mateial_id",
            "price_id",
            "amenities_id",
            "number_romm_id",
            "currency_id",
            "is_appropriate",
            "author_id",
            "distric_id",
            "status_id",
            "payment_id",
            "is_payment",
            "is_active",
            "apartment_area",
            "house_area",
            "floors_building",
            "price",
            "content",
            "img",
            "datetime",
        ]

    def create(self, validated_data):
        """RealEstate Create And Multiple Img Funcation"""
        img = validated_data.pop("img")
        amin = validated_data.pop('amenities_id')
        sm = validated_data.get('payment_id')
        real_estet = RealEstate.objects.create(**validated_data)
        real_estet.author_id = self.context.get("author_id")
        us = CustomUser.objects.filter(
            username=self.context.get("author_id"))[0]
        if int(us.summ) > int(sm.summ):
            us.summ = int(us.summ) - int(sm.summ)
            us.save()
        else:
            raise serializers.ValidationError(
                "The doctor is busy at the moment")

        for k in amin:
            real_estet.amenities_id.add(k)
        real_estet.save()
        for item in img:
            images = RealEstetImgaes.objects.create(
                real_estet_id=real_estet, img=item)
            images.save()
        return real_estet

    def update(self, instance, validated_data):
        """RealEstate Update Funcation"""
        instance.category_id = validated_data.get(
            "category_id", instance.category_id)
        instance.ad_taype_id = validated_data.get(
            "ad_taype_id", instance.ad_taype_id)
        instance.ad_subcategory_id = validated_data.get(
            "ad_subcategory_id", instance.ad_subcategory_id)
        instance.repair_id = validated_data.get(
            "repair_id", instance.repair_id)
        instance.build_mateial_id = validated_data.get(
            "build_mateial_id", instance.build_mateial_id)
        instance.price_id = validated_data.get("price_id", instance.price_id)
        instance.amenities_id = validated_data.get(
            "amenities_id", instance.amenities_id)
        instance.number_romm_id = validated_data.get(
            "number_romm_id", instance.number_romm_id)
        instance.currency_id = validated_data.get(
            "currency_id", instance.currency_id)

        instance.is_appropriate = validated_data.get(
            "is_appropriate", instance.is_appropriate)
        instance.distric_id = validated_data.get(
            "distric_id", instance.distric_id)
        instance.apartment_area = validated_data.get(
            "apartment_area", instance.apartment_area)
        instance.house_area = validated_data.get(
            "house_area", instance.house_area)
        instance.floors_building = validated_data.get(
            "floors_building", instance.floors_building)
        instance.price = validated_data.get("price", instance.price)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance


class RealEstetImgaesSerializers(serializers.ModelSerializer):
    """RealEstetImgaes Serializer"""

    img = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = RealEstetImgaes
        fields = ["id", "real_estet_id", "img"]

    def update(self, instance, validated_data):
        """RealEstate Update Funcation"""
        if instance.img == None:
            instance.img = self.context.get("img")
        else:
            instance.img = validated_data.get(
                    "img", instance.img)
        instance.save()
        return instance


class BuyRealEstetSerializers(serializers.ModelSerializer):
    """BuyRealEstet Serializer"""

    class Meta:
        model = BuyRealEstet
        fields = "__all__"


class SendBuyRealEstetSerializers(serializers.ModelSerializer):
    """BuyRealEstet Serializer"""

    class Meta:
        model = BuyRealEstet
        fields = ['id', 'user_id', 'real_estet_id']

    def create(self, validated_data):
        """BuyRealEstet Create Function"""
        real_estet = BuyRealEstet.objects.create(**validated_data)
        real_estet.user_id = self.context.get("user_id")
        real_estet.real_estet_id = self.context.get('real_estet_id')
        real_estet.save()
        return real_estet

    def update(self, instance, validated_data):
        """BuyRealEstet Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
