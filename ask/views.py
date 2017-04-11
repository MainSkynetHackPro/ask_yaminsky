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


class ByTagView(ListView):
    template_name = 'ask/by_tag_list.html'
    model = Ask
    paginate_by = 10

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return self.model.objects.filter(tags__pk=pk)

    def get_context_data(self, **kwargs):
        context = super(ByTagView, self).get_context_data(**kwargs)
        if not context['object_list']:
            raise Http404
        context['current_tag'] = Tag.objects.filter(pk=self.kwargs.get('pk')).first()
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