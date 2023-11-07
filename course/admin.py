from django.contrib import admin
from course.models import (
    CategoriesCourse,
    Course,
    CourseLesson,
    BuyCourse,
    TestLesson,
)


class NewCategoriesCourse(admin.ModelAdmin):
    model = CategoriesCourse
    list_display = ["id", "name"]


admin.site.register(CategoriesCourse, NewCategoriesCourse)


class NewCourse(admin.ModelAdmin):
    model = Course
    list_display = ["id", "name", "author_id", "category_id"]


admin.site.register(Course, NewCourse)


class NewCourseLesson(admin.ModelAdmin):
    model = CourseLesson
    list_display = ["id", "name"]


admin.site.register(CourseLesson, NewCourseLesson)


class NewBuyCourse(admin.ModelAdmin):
    model = BuyCourse
    list_display = ["id", "user_id", "course_id"]


admin.site.register(BuyCourse, NewBuyCourse)


class NewTestLesson(admin.ModelAdmin):
    model = TestLesson
    list_display = ["id", "lesson_id", "user_id"]


admin.site.register(TestLesson, NewTestLesson)
