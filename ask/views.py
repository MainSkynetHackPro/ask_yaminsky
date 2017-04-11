# coding=utf8
from django.views.generic import TemplateView, ListView, DetailView
from django.http import Http404
from ask.models import Ask, Tag


class AskListView(ListView):
    template_name = 'ask/list.html'
    model = Ask
    ordering = '-pk'
    paginate_by = 10


class TopAskListView(ListView):
    template_name = 'ask/top_list.html'
    model = Ask
    ordering = '-rating'
    paginate_by = 10

    def get_queryset(self):
        queryset = Ask.objects.top_questions()
        return queryset


class ByTagView(ListView):
    template_name = 'ask/by_tag_list.html'
    model = Ask
    paginate_by = 10

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Ask.objects.get_all_by_tag_pk(pk)
        if not queryset:
            raise Http404
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ByTagView, self).get_context_data(**kwargs)
        context['current_tag'] = Tag.objects.get_tag_by_pk(self.kwargs.get('pk'))
        return context


class QuestionView(DetailView):
    template_name = 'ask/answer.html'
    model = Ask


class CreateAskView(TemplateView):
    template_name = 'ask/create.html'


class ProfileView(TemplateView):
    template_name = 'profile/profile.html'


class LoginView(TemplateView):
    template_name = 'profile/login.html'


class RegistrationView(TemplateView):
    template_name = 'profile/registration.html'