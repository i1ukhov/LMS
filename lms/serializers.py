from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson, Subscription
from lms.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="link")]


class CourseSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField(read_only=True)
    content = LessonSerializer(many=True, source="course", read_only=True)
    subscription = SerializerMethodField(read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context.get("request").user
        subscription = Subscription.objects.filter(user=user, course=course)
        return subscription.exists()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "preview",
            "number_of_lessons",
            "content",
            "owner",
            "subscription",
        )


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
