""" Django DRF Packaging """
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from authen.renderers import UserRenderers
from authen.models import CustomUser, CheckSms
from django.db.models import Q
from authen.serializers import (
    UserGroupsSerializers,
    UserSigInUpSerializers,
    UserSigInInSerializers,
    UserInformationSerializers,
    ChangePasswordSerializer,
)


# JWT token refresh
def get_token_for_user(user):
    """Django Authe token"""
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}


class UserGroupsViews(APIView):
    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        queryset = Group.objects.filter(Q(name='student') | Q(name='teacher'))
        serializers = UserGroupsSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UserRegisterViews(APIView):
    """UserRegister Views"""

    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def post(self, request):
        serializer = UserSigInUpSerializers(
            data=request.data,
            context={"avatar": request.FILES.get("avatar", None)}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSigInViews(APIView):
    """ UserSigIn Views"""

    render_classes = [UserRenderers]

    def post(self, request):
        serializer = UserSigInInSerializers(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            username = request.data["username"]
            password = request.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                tokens = get_token_for_user(user)
                # sms_random = str(random.randint(10000, 99999))
                # send_sms(user.username, sms_random)
                # code_save = SmsCode(
                # user_id=request.user, sms_code=sms_random)
                # code_save.save()
                return Response(
                    {"token": tokens, "message": "Welcome to the system"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "error": {
                            "none_filed_error": [
                                "This user is not available to the system"
                            ]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckSmsCode(APIView):
    """Chack SMS class"""

    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def post(self, request):
        """Chack sms code verification"""

        sms_code = request.data["sms_code"]
        if sms_code == "":
            context = {"Code not entered"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
        code_objects = CheckSms.objects.latest("id")
        if int(sms_code) == int(code_objects.sms_code):
            context = {"Welcome to the system !"}
            return Response(context, status=status.HTTP_200_OK)
        return Response(
            {"error": "SMS code error"},
            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
        )


class UserProfilesViews(APIView):
    """User Pofiles classs"""

    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        """User information views"""
        serializer = UserInformationSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateView(APIView):
    """User PUT Class"""

    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def put(self, request):
        """User Update views"""
        queryset = get_object_or_404(CustomUser, id=request.user.id)
        serializer = UserSigInUpSerializers(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "update error data"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response(
                    {'message': 'Password changed successfully.'},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'error': 'Incorrect old password.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTeachersViews(APIView):
    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        queryset = CustomUser.objects.filter(groups__name__in=['teacher'])
        serializers = UserInformationSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UserStudentViews(APIView):
    render_classes = [UserRenderers]
    permission = [IsAuthenticated]

    def get(self, request):
        queryset = CustomUser.objects.filter(groups__name__in=['student'])
        serializers = UserInformationSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
