from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """Custom Users Table"""

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)


class CheckSms(models.Model):
    """SMS verification Table"""

    sms_code = models.IntegerField(default=0)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
        blank=True
    )
    datetime = models.DateTimeField(auto_now_add=True)


# class CategoriesCourse(models.Model):
#     """CategoriesCourse Table"""

#     name = models.CharField(max_length=100)
#     img = models.ImageField(upload_to="categories_course/", null=True, blank=True)


# class Course(models.Model):
#     """CategoriesCourse Table"""
#     name = models.CharField(max_length=100)
#     content = models.TextField()
#     course_logo = models.ImageField(upload_to="course_logo/")
#     category_id = models.ForeignKey(CategoriesCourse, on_delete=models.CASCADE)
#     summ_course = models.FloatField()
#     verification_course = models.BooleanField(default=False)
#     author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now_add=True)


# class CourseLesson(models.Model):
#     """CategoriesCourse Table"""
#     name = models.CharField(max_length=250)
#     content = models.TextField()
#     video = models.FileField(
#         upload_to="course_lesson/",
#         null=True,
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
#             )
#         ],
#     )
#     files = models.FileField(upload_to="course_lesson/", null=True, blank=True)
#     courser_id = models.ForeignKey(Course, on_delete=models.CASCADE)
#     datetime = models.DateTimeField(auto_now_add=True)


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
