from django.urls import path
from other_blog.views import (
    BlogListViews,
    BlogListCrudViews,
    MyBlogListViews,
)

urlpatterns = [
    path('blog_list_views/', BlogListViews.as_view()),
    path('blog_list_crud_views/<int:pk>/', BlogListCrudViews.as_view()),
    path('my_blog_list_views/', MyBlogListViews.as_view()),

]
