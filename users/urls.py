from users.apps import UsersConfig
from django.urls import path

from users.views import PaymentListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]
