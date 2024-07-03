from rest_framework.viewsets import ModelViewSet

from lms.serializers import UserSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
