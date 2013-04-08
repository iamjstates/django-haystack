# A couple models for Haystack to test with.
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class MockTag(models.Model):
    name = models.CharField(max_length=32)


@python_2_unicode_compatible
class MockModel(models.Model):
    author = models.CharField(max_length=255)
    foo = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    tag = models.ForeignKey(MockTag)

    def __str__(self):
        return self.author

    def hello(self):
        return 'World!'


@python_2_unicode_compatible
class AnotherMockModel(models.Model):
    author = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.author


class AThirdMockModel(AnotherMockModel):
    average_delay = models.FloatField(default=0.0)
    view_count = models.PositiveIntegerField(default=0)


class CharPKMockModel(models.Model):
    key = models.CharField(primary_key=True, max_length=10)


@python_2_unicode_compatible
class AFourthMockModel(models.Model):
    author = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.author


class SoftDeleteManager(models.Manager):
    def get_query_set(self):
        return super(SoftDeleteManager, self).get_query_set().filter(deleted=False)

    def complete_set(self):
        return super(SoftDeleteManager, self).get_query_set()


@python_2_unicode_compatible
class AFifthMockModel(models.Model):
    author = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.author


@python_2_unicode_compatible
class ASixthMockModel(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ScoreMockModel(models.Model):
    score = models.CharField(max_length=10)

    def __str__(self):
        return self.score
