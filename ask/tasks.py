# encoding=utf8
from celery.task import periodic_task
from celery.schedules import crontab
from django.core.cache import cache

from ask.models import User, UserVote, Ask, Answer, Tag
from datetime import timedelta
from django.db.models import Count
from django.utils import timezone
from random import shuffle
from django.template import Template, loader
from django.core.urlresolvers import reverse
from django.db.models import Q


@periodic_task(run_every=crontab(minute='*/1'))
def cache_top():
    tags = Tag.objects.filter(asks__answers__date_create__gte=timezone.now() - timedelta(days=30)).annotate(
        count=Count('title')).order_by('-count')[:10]

    min_value = tags[len(tags) - 1].count
    max_value = tags[0].count

    tags_list = []

    for tag in tags:
        tag_item = dict()
        tag_item["tag"] = tag.tag
        tag_item["value"] = int(
            round(float(float(tag.count - min_value + 1) / float(max_value - min_value + 1)) * float(8)))
        tag_item["pk"] = int(tag.pk),
        tags_list.append(tag_item)

    shuffle(tags_list)

    t = loader.get_template('blocks/popular_tags.html')
    context = {
        'tags_list': tags_list
    }
    cache.set('top_tags', t.render(context=context), timeout=None)

    users = User.object.filter(Q(asks__date_create__gte=timezone.now() - timedelta(days=30)) | Q(
        answers__date_create__gte=timezone.now() - timedelta(days=30))).annotate(
        count=Count('pk')).order_by('-count')[:10]

    t = loader.get_template('blocks/best_members.html')
    context = {
        'users': users,
    }
    cache.set('top_users', t.render(context=context), timeout=None)
