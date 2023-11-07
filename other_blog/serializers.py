from rest_framework import serializers
from authen.models import CustomUser
from other_blog.models import Blog


class UserInformationSerializers(serializers.ModelSerializer):
    """User Profiles Serializers"""

    class Meta:
        """User Model Fileds"""

        model = CustomUser
        fields = ["id", "first_name", "last_name", "email"]


class BlogListSerializers(serializers.ModelSerializer):

    author_id = UserInformationSerializers(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'


class BlogListCrudSerializers(serializers.ModelSerializer):
    """Course Serializer"""

    img = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )

    class Meta:
        model = Blog
        fields = ["title", "content", "img", "author_id"]

    def create(self, validated_data):
        """Create ExpeectedSalary"""
        create = Blog.objects.create(**validated_data)
        create.author_id = self.context.get("author_id")
        create.save()
        return create

    def update(self, instance, validated_data):
        """CategoriesCourse Update Function"""
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        if instance.img == None:
            instance.img = self.context.get("img")
        else:
            instance.img = validated_data.get(
                "img", instance.img)
        instance.save()
        return instance
