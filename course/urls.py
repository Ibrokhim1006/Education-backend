""" Django Libraries """
from django.urls import path
from course.views import (
    # Categories Course
    CategoriesCourseViews,
    CategoriesCourseCrudViews,
    # Course
    CourseViews,
    CourseCrudViews,
    AuthorCourseViews,
    UserCourseViews,
    CategoriesInCourseViews,
    # Course Lesson
    CourseLessonViews,
    CourseLessonCrudViews,
    # Buy course
    BuyCourseViews,
    TestLessonViews,
    TestLessonCrudViews,
)

urlpatterns = [
    path('categories_course_views/', CategoriesCourseViews.as_view()),
    path(
        'categories_course_crud_views/<int:pk>/',
        CategoriesCourseCrudViews.as_view()),
    # Course
    path('course_views/', CourseViews.as_view()),
    path('course_crud_views/<int:pk>/', CourseCrudViews.as_view()),
    path('author_course_views/', AuthorCourseViews.as_view()),
    path('user_course_views/', UserCourseViews.as_view()),
    path('categories_in_course_views/', CategoriesInCourseViews.as_view()),
    # Course Lesson
    path('course_lesson_views/<int:pk>/', CourseLessonViews.as_view()),
    path(
        'course_lesson_crud_views/<int:pk>/', CourseLessonCrudViews.as_view()),
    # Buy Course
    path('buy_course_views/', BuyCourseViews.as_view()),
    path('test_lesson_views/<int:pk>/', TestLessonViews.as_view()),
    path('test_lesson_crud_views/<int:pk>/', TestLessonCrudViews.as_view()),

]
