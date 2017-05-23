# encoding=utf8

from django.core.management.base import BaseCommand

from ask.tasks import cache_top


class Command(BaseCommand):
    def handle(self, *args, **options):
        cache_top()