# coding=utf8
from django.views.generic import TemplateView


class AskListView(TemplateView):
    template_name = 'ask/list.html'

    def get_context_data(self, **kwargs):
        context = super(AskListView, self).get_context_data()

        data = []

        for i in range(10):
            item = dict()
            item['username'] = u'username'
            item['question'] = u'Some question?'
            item['rating'] = 5
            data.append(item)

        context['object_list'] = data
        return context


class QuestionView(TemplateView):
    template_name = 'ask/answer.html'


class CreateAskView(TemplateView):
    template_name = 'ask/create.html'


class ProfileView(TemplateView):
    template_name = 'profile/profile.html'


class LoginView(TemplateView):
    template_name = 'profile/login.html'


class RegistrationView(TemplateView):
    template_name = 'profile/registration.html'