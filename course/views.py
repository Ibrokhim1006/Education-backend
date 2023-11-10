""" Django DRF Packaging """
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authen.renderers import UserRenderers
from authen.pagination import PageNumberPagination
from authen.models import CustomUser
from course.models import (
    CategoriesCourse,
    Course,
    CourseLesson,
    BuyCourse,
    TestLesson
)
from course.serializers import (
    # Categories Course
    CategoriesCourseSerializers,
    CategoriesCourseCrudSerializers,
    # Course
    CourseSerializers,
    CourseCrudSerializers,
    LessonCourseSerializers,
    # Course Lesson
    CourseLessonSerializers,
    CourseLessonCrudSerializers,
    # buy course
    BuyCourseSerializers,
    BuyCourseCrudSerializers,
    TestLessonSerializers,
    TestLessonCrudSerializers,
)


# Categories Course
class CategoriesCourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = CategoriesCourseSerializers

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
        instance = CategoriesCourse.objects.all().order_by("pk")
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
        serializers = CategoriesCourseCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img=request.data.get("img"))
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesCourseCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = CategoriesCourse.objects.filter(id=pk)
        serializers = CategoriesCourseSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = CategoriesCourseCrudSerializers(
            instance=CategoriesCourse.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(img=request.data.get("img"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        objects_get = CategoriesCourse.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


# Course
class CourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = CourseSerializers

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
        instance = Course.objects.filter(verification_course=True)
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

    def post(self, request):
        """Course POST views"""
        serializer = CourseCrudSerializers(
            data=request.data,
            context={
                "author_id": request.user,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Course.objects.filter(id=pk)
        serializers = LessonCourseSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = CourseCrudSerializers(    
            instance=Course.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = Course.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


class AuthorCourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        instance = Course.objects.filter(author_id=request.user).order_by("pk")
        serializer = CourseSerializers(instance, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class UserCourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        instance = BuyCourse.objects.filter(user_id=request.user)
        serializer = BuyCourseSerializers(instance, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class CategoriesInCourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = CategoriesCourseSerializers

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

    def get(self, request, pk):
        instance = Course.objects.filter(category_id=pk).order_by("pk")
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


class CourseNoActiViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request):
        instance = Course.objects.filter(verification_course=False)
        ls = []
        for item in instance:
            ls.append({
                'id': item.id,
                'name': item.name,
                "verification_course": item.verification_course})
        return Response({'data': ls}, status=status.HTTP_200_OK)


class ActiveateCourseCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = Course.objects.filter(id=pk)
        serializers = LessonCourseSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = Course.objects.filter(id=pk)[0]
        instance.verification_course = True
        instance.save()
        return Response(
            {"Message": "update"}, status=status.HTTP_200_OK
        )


# Course Lesson
class CourseLessonViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = CourseLessonSerializers

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

    def get(self, request, pk):
        instance = CourseLesson.objects.filter(courser_id=pk).order_by("pk")
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

    def post(self, request, pk):
        """Course POST views"""
        course = Course.objects.filter(id=pk)[0]
        serializer = CourseLessonCrudSerializers(
            data=request.data,
            context={
                "courser_id": course,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseLessonCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = CourseLesson.objects.filter(id=pk)
        serializers = CourseLessonSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = CourseLessonCrudSerializers(
            instance=CourseLesson.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = CourseLesson.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)


# Buy Course
class BuyCourseViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = PageNumberPagination
    serializer_class = BuyCourseSerializers

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

    def get(self, request):
        instance = BuyCourse.objects.all()
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

    def post(self, request):
        """ Buy Course POST views"""
        serializer = BuyCourseCrudSerializers(
            data=request.data,
            context={
                "user_id": request.user,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TestLessonViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        instance = TestLesson.objects.filter(lesson_id=pk)
        serializer = TestLessonSerializers(instance, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, pk):
        """ Buy Course POST views"""
        tests = TestLesson.objects.filter(id=pk)[0]
        serializer = TestLessonCrudSerializers(
            data=request.data,
            context={
                "user_id": request.user,
                "lesson_id": tests,
            },
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TestLessonCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk):
        objects_list = TestLesson.objects.filter(id=pk)
        serializers = TestLessonSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializers = TestLessonCrudSerializers(
            instance=TestLesson.objects.filter(id=pk)[0],
            data=request.data, partial=True
        )
        if serializers.is_valid(raise_exception=True):
            serializers.save(course_logo=request.data.get("course_logo"))
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        objects_get = TestLesson.objects.get(id=pk)
        objects_get.delete()
        return Response(
            {"message": "Delete success"}, status=status.HTTP_200_OK)
