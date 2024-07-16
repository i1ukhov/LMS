from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson
from lms.validators import LinkValidator
from users.models import User


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="link")]


class CourseSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField(read_only=True)
    content = LessonSerializer(many=True, source="course", read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

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
        )
