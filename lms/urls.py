from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView,
                       LessonDestroyAPIView, LessonListAPIView,
                       LessonRetrieveAPIView, LessonUpdateAPIView)
from users.views import UserViewSet

app_name = LmsConfig.name
router = SimpleRouter()
router.register(r"courses", CourseViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"
    ),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lessons_delete",
    ),
] + router.urls
