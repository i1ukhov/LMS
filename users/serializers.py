from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaymentSerializer(many=True, source="user")

    class Meta:
        model = User
        fields = "__all__"
