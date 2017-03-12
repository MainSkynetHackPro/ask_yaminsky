from django import template
from django.template import loader

register = template.Library()


@register.simple_tag(takes_context=True)
def popular_tags(context):
    request = context['request']
    t = loader.get_template('blocks/popular_tags.html')
    context = {}
    return t.render(context=context)


@register.simple_tag(takes_context=True)
def best_members(context):
    request = context['request']
    t = loader.get_template('blocks/best_members.html')
    context = {}
    return t.render(context=context)
