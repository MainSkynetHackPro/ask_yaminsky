# encoding=utf8
from django.db import models
from django.conf import settings


class TagManager(models.Manager):
    def get_tag_by_pk(self, pk):
        return self.filter(pk=pk).first()


class AskManager(models.Manager):
    def get_all_by_tag_pk(self, pk):
        return self.filter(tags__pk=pk)

    def top_questions(self):
        return self.filter(rating__gte=settings.TOP_RATING).order_by('-rating')