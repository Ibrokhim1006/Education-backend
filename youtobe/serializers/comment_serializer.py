""" Django Rest Framework Library """
from rest_framework import serializers

""" Authentification Serializer """
from youtobe.models import (
    Explore,
    Videos,
    Comments,
    UserViews
)
from youtobe.serializers.explore_serializer import (
    ExploreListSerializer,
)
from youtobe.serializers.video_serializer import (
    VideoListSerializer,
    VideoDetailSerializer,
)
from authen.serializers import (
    UserInformationSerializers
)



class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = [
            'username',
            'video',
            'describe',
        ]

        def create(self, validated_data):

            create = Comments.objects.create(**validated_data)
            return create


class CommentDetailSerializer(serializers.ModelSerializer):
    username = UserInformationSerializers(read_only=True)
    video = VideoDetailSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = [
            'username',
            'video',
            'describe',
            'post_date'
        ]


class HistorySerializer(serializers.ModelSerializer):
    username = UserInformationSerializers(read_only=True)
    video = VideoDetailSerializer(read_only=True)

    class Meta:
        model = UserViews
        fields = (
            'username',
            'video',
            'post_date'
        )


class HistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserViews
        fields = [
            'username',
            'video',
            'post_date'
        ]

        def create(self, validated_data):

            create = UserViews.objects.create(**validated_data)
            return create