from rest_framework import serializers

from users.models import Payment, User
from users.services import retrieve_sessions_statuses


class PaymentSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}

    def get_payment_status(self, obj):
        """Получение статуса платежной сессии в Stripe."""

        if obj.session_id is not None:
            return retrieve_sessions_statuses(obj.session_id)
        return "сессия некорректна"


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "avatar",
            "payment_history",
        )
