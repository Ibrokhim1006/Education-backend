from rest_framework import serializers
from authen.models import CustomUser
from course.models import (
    CategoriesCourse,
    Course,
    CourseLesson,
    BuyCourse,
    TestLesson,
)


class UserInformationSerializers(serializers.ModelSerializer):
    """User Profiles Serializers"""

    class Meta:
        """User Model Fileds"""

        model = CustomUser
        fields = ["id", "first_name", "last_name", "email"]


# Categories
class CategoriesCourseSerializers(serializers.ModelSerializer):
    """CategoriesCourse Serializer"""

    class Meta:
        model = CategoriesCourse
        fields = "__all__"


class CategoriesCourseCrudSerializers(serializers.ModelSerializer):
    """CategoriesCourse Serializer"""

    img = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = CategoriesCourse
        fields = "__all__"

    def create(self, validated_data):
        """CategoriesCourse Create Function"""
        return CategoriesCourse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """CategoriesCourse Update Function"""
        instance.name = validated_data.get("name", instance.name)
        if instance.img == None:
            instance.img = self.context.get("img")
        else:
            instance.img = validated_data.get("img", instance.img)
        instance.save()
        return instance


# Course
class CourseSerializers(serializers.ModelSerializer):
    """Course Serializer"""

    category_id = CategoriesCourseSerializers(read_only=True)
    author_id = UserInformationSerializers(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseCrudSerializers(serializers.ModelSerializer):
    """Course Serializer"""

    course_logo = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = Course
        fields = [
            "name",
            "content",
            "course_logo",
            "category_id",
            "summ_course",
            "verification_course",
            "author_id",
        ]

        def create(self, validated_data):
            """Create ExpeectedSalary"""

            create = Course.objects.create(**validated_data)
            create.author_id = self.context.get("author_id")
            create.save()
            return create

        def update(self, instance, validated_data):
            """CategoriesCourse Update Function"""
            instance.name = validated_data.get("name", instance.name)
            instance.content = validated_data.get("content", instance.content)
            instance.category_id = validated_data.get(
                "category_id", instance.category_id)
            instance.summ_course = validated_data.get(
                "summ_course", instance.summ_course)
            instance.verification_course = validated_data.get(
                "verification_course", instance.verification_course)
            if instance.course_logo == None:
                instance.course_logo = self.context.get("course_logo")
            else:
                instance.course_logo = validated_data.get(
                    "course_logo", instance.course_logo)
            instance.save()
            return instance


# Course Lesson
class CoursesSerializers(serializers.ModelSerializer):
    """Course Serializer"""

    class Meta:
        model = Course
        fields = ['id', 'name']


class CourseLessonSerializers(serializers.ModelSerializer):
    """Course Lesson Serializer"""
    courser_id = CoursesSerializers(read_only=True)

    class Meta:
        model = CourseLesson
        fields = "__all__"


class CourseLessonCrudSerializers(serializers.ModelSerializer):
    """Course Lesson Serializer"""
    video = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )
    files = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = CourseLesson
        fields = ["name", "content", "video", "files", "courser_id"]

    def create(self, validated_data):
        """Create ExpeectedSalary"""
        create = CourseLesson.objects.create(**validated_data)
        create.courser_id = self.context.get("courser_id")
        create.save()
        return create

    def update(self, instance, validated_data):
        """CategoriesCourse Update Function"""
        instance.name = validated_data.get("name", instance.name)
        instance.content = validated_data.get("content", instance.content)
        if instance.video == None:
            instance.video = self.context.get("video")
        else:
            instance.video = validated_data.get(
                "video", instance.video)
        if instance.files == None:
            instance.files = self.context.get("files")
        else:
            instance.files = validated_data.get(
                "files", instance.files)
        instance.save()
        return instance


# Buy Course
class BuyCourseSerializers(serializers.ModelSerializer):
    """ Buy Course Serializer"""
    course_id = CourseSerializers(read_only=True)
    user_id = UserInformationSerializers(read_only=True)

    class Meta:
        model = BuyCourse
        fields = "__all__"


class BuyCourseCrudSerializers(serializers.ModelSerializer):
    """ Buy Course Serializer"""

    class Meta:
        model = BuyCourse
        fields = ["user_id", "course_id"]

    def create(self, validated_data):
        """Create BuyCourse"""
        create = BuyCourse.objects.create(**validated_data)
        create.user_id = self.context.get("user_id")
        create.save()
        return create


class LessonCourseSerializers(serializers.ModelSerializer):
    """Course Serializer"""
    course = CourseLessonSerializers(many=True, read_only=True)
    category_id = CategoriesCourseSerializers(read_only=True)
    author_id = UserInformationSerializers(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class TestLessonSerializers(serializers.ModelSerializer):
    """Course Serializer"""
    lesson_id = CourseLessonSerializers(many=True, read_only=True)
    user_id = UserInformationSerializers(read_only=True)

    class Meta:
        model = TestLesson
        fields = "__all__"


class TestLessonCrudSerializers(serializers.ModelSerializer):
    """Test Serializer"""
    files = serializers.FileField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = TestLesson
        fields = ["lesson_id", "user_id", "files", "is_active"]

    def create(self, validated_data):
        """Create Test"""
        create = TestLesson.objects.create(**validated_data)
        create.user_id = self.context.get("user_id")
        create.lesson_id = self.context.get('lesson_id')
        create.save()
        return create

    def update(self, instance, validated_data):
        """CategoriesCourse Update Function"""
        instance.is_active = validated_data.get(
            "is_active", instance.is_active)
        if instance.files == None:
            instance.files = self.context.get("files")
        else:
            instance.files = validated_data.get(
                "files", instance.files)
        instance.save()
        return instance
