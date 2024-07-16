from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = dict(value).get(self.field)
        if "https://www.youtube.com/" not in link:
            raise ValidationError("Ссылка должна быть на материал с YouTube")
