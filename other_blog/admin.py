from django.contrib import admin
from other_blog.models import Blog


class NewBlog(admin.ModelAdmin):
    model = Blog
    list_display = ["id", "title", "author_id"]


admin.site.register(Blog, NewBlog)
