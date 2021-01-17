import os
from uuid import uuid4

from django.db import models
from django.utils.deconstruct import deconstructible

from sigmage import get_signature, set_signature


@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        return os.path.join(self.sub_path, f'{uuid4().hex}.{ext}')


class Query(models.Model):
    image = models.ImageField(upload_to=UploadToPathAndRename('images/'))

    @property
    def signature(self):
        return get_signature(self.image.path)

    @signature.setter
    def signature(self, signature):

        set_signature(self.image.path, self.image.path, signature)

    class Meta:
        verbose_name_plural = 'queries'
