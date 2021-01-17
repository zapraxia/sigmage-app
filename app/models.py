from django.db import models
from uuid import uuid4

from sigmage import get_signature, set_signature
from django_sos.utils import UploadHexTo

from django.db.models import Model


class Query(models.Model):
    upload_to = 'images/'

    image = models.ImageField(upload_to=UploadHexTo(upload_to))

    @property
    def signature(self):
        return get_signature(self.image.path)

    @signature.setter
    def signature(self, signature):
        prev_image_path = self.image.path
        self.image.name = f'{self.upload_to}/{uuid4().hex}.png'
        set_signature(prev_image_path, self.image.path, signature)

    class Meta:
        verbose_name_plural = 'queries'
