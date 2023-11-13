from django.db import models
from django.conf import settings
from authen.models import PyemntSumm


class Currency(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Distric(models.Model):
    name = models.CharField(max_length=100)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoriesRealEstet(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class AdType(models.Model):
    name = models.CharField(max_length=100)
    id_category = models.ForeignKey(
        CategoriesRealEstet, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AdSubCategory(models.Model):
    name = models.CharField(max_length=250)
    id_ad_type = models.ForeignKey(
        AdType, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Repair(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BuildMaterial(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Amenities(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NumberRooms(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RealEstate(models.Model):
    category_id = models.ForeignKey(
        CategoriesRealEstet, on_delete=models.CASCADE, null=True, blank=True)
    ad_taype_id = models.ForeignKey(
        AdType, on_delete=models.CASCADE, null=True, blank=True)
    ad_subcategory_id = models.ForeignKey(
        AdSubCategory, on_delete=models.CASCADE, null=True, blank=True)
    repair_id = models.ForeignKey(
        Repair, on_delete=models.CASCADE, null=True, blank=True)
    build_mateial_id = models.ForeignKey(
        BuildMaterial, on_delete=models.CASCADE, null=True, blank=True)
    price_id = models.ForeignKey(
        Price, on_delete=models.CASCADE, null=True, blank=True)
    amenities_id = models.ManyToManyField(Amenities, null=True, blank=True)
    number_romm_id = models.ForeignKey(
        NumberRooms, on_delete=models.CASCADE, null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, null=True, blank=True)
    is_appropriate = models.BooleanField(default=False)
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, blank=True)
    distric_id = models.ForeignKey(
        Distric, on_delete=models.CASCADE, null=True, blank=True)
    status_id = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True, blank=True)
    payment_id = models.ForeignKey(
        PyemntSumm, on_delete=models.CASCADE, null=True, blank=True)
    # kvarira
    apartment_area = models.CharField(
        max_length=30, null=True, blank=True
    )  # yer maydun
    house_area = models.CharField(
        max_length=30, null=True, blank=True)  # uy maydoni
    floors_building = models.CharField(
        max_length=20, null=True, blank=True
    )  # uy qavati
    price = models.FloatField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_payment = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)


class RealEstetImgaes(models.Model):
    real_estet_id = models.ForeignKey(
        RealEstate, on_delete=models.CASCADE, related_name='img')
    img = models.ImageField(upload_to="home/", null=True, blank=True)


class BuyRealEstet(models.Model):
    real_estet_id = models.ForeignKey(
        RealEstate, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
