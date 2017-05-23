from django import template
from django.template import loader
from django.core.cache import cache

register = template.Library()


@register.simple_tag(takes_context=True)
def popular_tags(context):
    return cache.get('top_tags')


@register.simple_tag(takes_context=True)
def best_members(context):
    return cache.get('top_users')
