from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="lms/courses_previews", help_text="Загрузите превью", **NULLABLE
    )
    description = models.TextField(
        max_length=250, verbose_name="Описание", help_text="Добавьте описание курса"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Добавьте описание урока"
    )
    preview = models.ImageField(
        upload_to="lms/lessons_preview",
        verbose_name="Превью",
        help_text="Загрузите превью",
        **NULLABLE,
    )
    link = models.URLField(
        max_length=200,
        verbose_name="Ссылка на видео",
        help_text="Добавьте ссылку на видео",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберите курс", related_name="course"
    )

    def __str__(self):
        return f"Урок {self.name} из курса {self.course}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
