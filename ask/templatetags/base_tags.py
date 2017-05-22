from django import template

register = template.Library()


@register.filter
def get_user_vote(item, user):
    vote = item.votes.filter(author=user).first()
    if not vote:
        return 0
    else:
        return vote.delta