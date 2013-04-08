from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Foo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Bar(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.author
