# encoding=utf8

from django.core.management.base import BaseCommand

from ask.tasks import cache_top
from channels import Group
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        Group('answers').send({
            'text': json.dumps({
                'title': 'asd',
                'author': 'qwe',
            })
        })
