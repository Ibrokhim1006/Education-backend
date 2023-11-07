from django.db import models
from django.conf import settings


class CategoriesCourse(models.Model):
    """CategoriesCourse Table"""

    name = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to="categories_course/", null=True, blank=True)


class Course(models.Model):
    """CategoriesCourse Table"""

    name = models.CharField(max_length=100)
    content = models.TextField()
    course_logo = models.ImageField(upload_to="course_logo/")
    category_id = models.ForeignKey(CategoriesCourse, on_delete=models.CASCADE)
    summ_course = models.FloatField()
    verification_course = models.BooleanField(default=False)
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class CourseLesson(models.Model):
    """CategoriesCourse Table"""

    name = models.CharField(max_length=250)
    content = models.TextField()
    video = models.FileField(
        upload_to="course_lesson/",
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to="course_lesson_file/", null=True, blank=True)
    courser_id = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        null=True, blank=True, related_name="course")
    datetime = models.DateTimeField(auto_now_add=True)


class BuyCourse(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True)
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


class TestLesson(models.Model):
    lesson_id = models.ForeignKey(CourseLesson, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True)
    files = models.FileField(upload_to='tests/')
    is_active = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
