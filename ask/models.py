# encoding=utf8
from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
import hashlib
import os

from ask.managers import TagManager, AskManager


def avatar_dir_path(instance, filename):
    name, extension = os.path.splitext(filename)
    hsh = hashlib.md5()
    hsh.update(str(timezone.now()))
    filename = u'{0}{1}'.format(hsh.hexdigest(), extension)
    return 'avatar/{0}/{1}/{2}/{3}'.format(filename[:2], filename[2:4], filename[4:6], filename[6:])


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=u'Username', max_length=255, unique=True, default=None,
                                error_messages={'unique': 'User with this username exists'})
    email = models.EmailField(verbose_name=u'Email', unique=True, default=None)

    is_staff = models.BooleanField(verbose_name=u'has admin access', default=False)

    avatar = models.ImageField(verbose_name=u'Avatar', upload_to=avatar_dir_path, default=None, blank=True, null=True)

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

    objects = TagManager()

    class Meta:
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'

    def __unicode__(self):
        return u'#{0}'.format(self.title)

    def tag(self):
        return u'#{0}'.format(self.title)


class Ask(models.Model):
    question = models.CharField(verbose_name=u'question', max_length=255)
    text = models.TextField(verbose_name=u'text', )
    rating = models.IntegerField(verbose_name=u'Rating', default=0)

    author = models.ForeignKey(User, verbose_name=u'Author', related_name=u'asks')

    tags = models.ManyToManyField(Tag, verbose_name=u'Tags', related_name=u'asks', blank=True)

    date_create = models.DateTimeField(verbose_name=u'Create date', default=timezone.now)

    objects = AskManager()

    class Meta:
        verbose_name = u'Ask'
        verbose_name_plural = u'Asks'

    def __unicode__(self):
        return self.question

    def has_correct_answers(self):
        if self.answers.filter(is_correct=True).count() > 0:
            return True
        return False


class Answer(models.Model):
    text = models.TextField(verbose_name=u'Answers')
    rating = models.IntegerField(verbose_name=u'Rating', default=0)

    ask = models.ForeignKey(Ask, verbose_name=u'Ask', related_name='answers')
    author = models.ForeignKey(User, verbose_name=u'Author', related_name=u'answers')

    date_create = models.DateTimeField(verbose_name=u'Create date', default=timezone.now)

    is_correct = models.BooleanField(verbose_name=u'Correct answer', default=False)

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

    date_create = models.DateTimeField(verbose_name=u'Create date', default=timezone.now)

    class Meta:
        verbose_name = u'User vote'
        verbose_name_plural = u'User votes'

    def __unicode__(self):
        return u'{0} [{1}]'.format(self.author.username, self.delta)
