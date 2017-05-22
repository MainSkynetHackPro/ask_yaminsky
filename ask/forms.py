# encoding=utf8
from django.forms import ModelForm
from django import forms
from ask.models import User, Ask, Tag
import re


class RegistrationForm(ModelForm):
    repeat_password = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        super(RegistrationForm, self).clean()
        if not self.errors:
            password = self.cleaned_data['password']
            repeat_password = self.cleaned_data['repeat_password']
            username = self.cleaned_data['username']
            if not re.match(r'^[a-zA-Z0-9-]{4,20}$', username):
                self.add_error('username',
                               u'Username must be more than 4 characters long and should consist of Latin letters or numbers')
            if password and password != repeat_password:
                self.add_error('repeat_password', u'Passwords does not match')

    def save(self, commit=True):
        instance = super(RegistrationForm, self).save(commit=False)

        user = User.object.create_user(
            instance.username,
            instance.email,
            instance.password
        )
        return user


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class AskForm(ModelForm):
    tags_list = forms.CharField(label='Tags')
    request = None

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Ask
        fields = ('question', 'text')

    def clean(self):
        super(AskForm, self).clean()

    def save(self, commit=True):
        instance = super(AskForm, self).save(commit=False)

        if commit:
            instance.author = self.request.user
            tags = self.data['tags_list']
            instance.save()
            if tags:
                tags_list = tags.split(" ")
                for tag in tags_list:
                    print tag
                    t_item, created = Tag.objects.get_or_create(title=tag)
                    print t_item
                    instance.tags.add(t_item)

        return instance