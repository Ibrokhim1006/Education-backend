""" Django DRF Packaging """
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authen.renderers import UserRenderers
from authen.pagination import PageNumberPagination
from other_blog.models import Blog
from other_blog.serializers import (
    BlogListSerializers,
    BlogListCrudSerializers,
)


class BlogListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = BlogListSerializers

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(
            queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None, *args, **kwargs):
        instance = Blog.objects.all().order_by("pk")
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(
            {"data": serializer.data, "page_number": self.paginator.page_size},
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        serializers = BlogListCrudSerializers(data=request.data)
        if serializers.is_valid(
            raise_exception=True,
            context={
                "author_id": request.user, },):
            serializers.save(img=request.data.get("img"))
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Blog.objects.filter(id=pk)
        serializers = BlogListSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = BlogListCrudSerializers(
            instance=Blog.objects.filter(id=pk, author_id=request.user)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = Blog.objects.get(id=pk, author_id=request.user)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class MyBlogListViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = BlogListSerializers

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(
            queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None, *args, **kwargs):
        instance = Blog.objects.filter(author_id=request.user).order_by("pk")
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(
            {"data": serializer.data, "page_number": self.paginator.page_size},
            status=status.HTTP_200_OK,
        )
