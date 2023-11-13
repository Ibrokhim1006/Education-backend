from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path("project/edu-app/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("project/edu-app/api/admin/", admin.site.urls),
    path(
        "project/edu-app/api/token/", jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "project/edu-app/api/token/refresh/", jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        "project/edu-app/api/docs/",
        TemplateView.as_view(
            template_name="doc.html",
            extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),
    path(
        "project/edu-app/api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("project/edu-app/api/authen/api/", include("authen.urls")),
    path('project/edu-app/api/course/api/', include('course.urls')),
    path('project/edu-app/api/others_blogs/api/', include('other_blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
