from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentCreateAPIView, PaymentListAPIView,
                         UserCreateAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_profile"),
]
