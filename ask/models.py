# encoding=utf8
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=u'Username', max_length=255, unique=True, default=None,
                                error_messages={'unique': 'User with this username exists'})
    email = models.EmailField(verbose_name=u'Email', unique=True, default=None, null=True, blank=True)

    is_staff = models.BooleanField(verbose_name=u'has admin access', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = UserManager()

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'
        swappable = 'AUTH_USER_MODEL'

    def __unicode__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username


class Tag(models.Model):
    title = models.CharField(verbose_name=u'Tag title', max_length=255, unique=True)

    class Meta:
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'

    def __unicode__(self):
        return u'#{0}'.format(self.title)


class Ask(models.Model):
    question = models.CharField(verbose_name=u'question', max_length=255)
    text = models.TextField(verbose_name=u'text', )
    rating = models.IntegerField(verbose_name=u'Rating', default=0)

    author = models.ForeignKey(User, verbose_name=u'Author')

    tags = models.ManyToManyField(Tag, verbose_name=u'Tags', blank=True)

    class Meta:
        verbose_name = u'Ask'
        verbose_name_plural = u'Asks'

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    text = models.TextField(verbose_name=u'Text')
    rating = models.IntegerField(verbose_name=u'Rating', default=0)

    ask = models.ForeignKey(Ask, verbose_name=u'Ask', related_name='answers')
    author = models.ForeignKey(User, verbose_name=u'Author')

    class Meta:
        verbose_name = u'Answer'
        verbose_name_plural = u'Answers'

    def __unicode__(self):
        return self.text


class UserVote(models.Model):
    author = models.ForeignKey(User, verbose_name=u'Author')
    ask = models.ForeignKey(Ask, verbose_name=u'Ask', related_name='votes', null=True, blank=True)
    answer = models.ForeignKey(Answer, verbose_name=u'Answer', related_name='votes', null=True, blank=True)

    delta = models.IntegerField(verbose_name=u'delta')

    class Meta:
        verbose_name = u'User vote'
        verbose_name_plural = u'User votes'

    def __unicode__(self):
        return u'{0} [{1}]'.format(self.author.username, self.delta)
