from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@test.test")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course"
        )
        self.lesson = Lesson.objects.create(
            name="Test Lesson",
            description="Test Lesson",
            link="https://www.youtube.com/",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """ "Тестирование просмотра урока."""
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("course"), self.lesson.course.pk)

    def test_lesson_create(self):
        """ "Тестирование создания урока."""
        url = reverse("lms:lessons_create")
        data = {
            "name": "Test1",
            "description": "Test1",
            "link": "https://www.youtube.com/",
            "course": self.lesson.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), "Test1")
        self.assertEqual(response.data.get("course"), self.lesson.course.pk)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """ "Тестирование обновления урока."""
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Test2",
        }
        response = self.client.patch(url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "Test2")
        self.assertEqual(response.data.get("course"), self.course.pk)

    def test_lesson_delete(self):
        """ "Тестирование удаления урока."""
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@test.test")
        self.course = Course.objects.create(
            title="Test Course", description="Test Course"
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("lms:subscription_create")

    def test_subscription_create(self):
        """Тестирование создания подписки."""
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_sub_delete(self):
        """Тестирование удаления подписки."""
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
