from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet


app_name = LmsConfig.name
router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [

]+router.urls
