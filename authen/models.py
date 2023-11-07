from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """Custom Users Table"""
    summ = models.FloatField(default=0, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)


class CheckSms(models.Model):
    """SMS verification Table"""

    sms_code = models.IntegerField(default=0)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
        blank=True
    )
    datetime = models.DateTimeField(auto_now_add=True)


# class BuyCourse(models.Model):
#     """CategoriesCourse Table"""
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now_add=True)


# class Blog(models.Model):
#     """CategoriesCourse Table"""
#     title = models.CharField(max_length=250)
#     content = models.TextField()
#     img = models.ImageField(upload_to='blog/')
#     author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now_add=True)
