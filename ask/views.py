# coding=utf8
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView

from ask.forms import RegistrationForm, ProfileForm, AskForm, AnswerForm
from ask.models import Ask, Tag, UserVote, Answer


class AskListView(ListView):
    # template_name = 'ask/list.html'
    model = Ask
    ordering = '-pk'
    paginate_by = 10

    def get_queryset(self):
        queryset = Ask.objects.all()
        return queryset


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


class QuestionView(FormView, DetailView):
    template_name = 'ask/answer.html'
    model = Ask
    form_class = AnswerForm

    def post(self, request, *args, **kwargs):
        self.object = None
        if self.request.user.is_authenticated():
            return super(QuestionView, self).post(request, *args, **kwargs)
        else:
            raise Http404

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.ask = Ask.objects.filter(pk=self.kwargs.get('pk')).first()
        instance.save()
        return HttpResponseRedirect(reverse("ask:show", kwargs={'pk': instance.ask.pk}))


class CreateAskView(LoginRequiredMixin, FormView):
    template_name = 'ask/create.html'
    form_class = AskForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(CreateAskView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        instance = form.save(commit=True)
        return HttpResponseRedirect(reverse("ask:show", kwargs={'pk': instance.pk}))


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/profile.html'
    form_class = ProfileForm
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super(ProfileView, self).form_valid(form)


class LoginView(TemplateView):
    template_name = 'profile/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_to = request.GET.get('next')
        user = authenticate(username=username, password=password)
        if user is None:
            context = self.get_context_data()
            context['form_error'] = u'Wrong username or password'
            return self.render_to_response(context)
        else:
            login(request, user)
        if not redirect_to:
            redirect_to = '/'
        return HttpResponseRedirect(redirect_to)


@login_required
@require_http_methods(["POST"])
def vote_ask(request):
    try:
        ask_id = int(request.POST.get('id'))
        delta = int(request.POST.get('delta'))
    except ValueError:
        raise Http404
    except TypeError:
        raise Http404
    data = dict()

    data['error'] = True
    data['message'] = 'Something gone wrong'

    if delta == 1 or delta == -1:

        ask = Ask.objects.filter(pk=ask_id).first()

        if not ask:
            raise Http404

        votes = ask.votes.all()
        if ask.votes.filter(author=request.user).count() > 0:
            data['error'] = True
            data['message'] = 'Already voted'
        else:
            vote = UserVote(author=request.user, ask=ask, delta=delta)
            vote.save()

            rating = 0
            for v in votes:
                rating += v.delta
            ask.rating = rating
            ask.save()
            data['error'] = False
            data['message'] = 'Ask successfully voted'
            data['rating'] = rating

    return HttpResponse(json.dumps(data))


@login_required
@require_http_methods(["POST"])
def vote_answer(request):
    try:
        answer_id = int(request.POST.get('id'))
        delta = int(request.POST.get('delta'))
    except ValueError:
        raise Http404
    except TypeError:
        raise Http404
    data = dict()

    data['error'] = True
    data['message'] = 'Something gone wrong'

    if delta == 1 or delta == -1:

        answer = Answer.objects.filter(pk=answer_id).first()

        if not answer:
            raise Http404

        votes = answer.votes.all()
        if answer.votes.filter(author=request.user).count() > 0:
            data['error'] = True
            data['message'] = 'Already voted'
        else:
            vote = UserVote(author=request.user, answer=answer, delta=delta)
            vote.save()

            rating = 0
            for v in votes:
                rating += v.delta
            answer.rating = rating
            answer.save()
            data['error'] = False
            data['message'] = 'Answer successfully voted'
            data['rating'] = rating

    return HttpResponse(json.dumps(data))


def logout_view(request):
    logout(request)
    return_to = request.META.get('HTTP_REFERER')
    if not return_to:
        return_to = '/'
    return HttpResponseRedirect(return_to)


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'profile/registration.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return super(RegistrationView, self).get(request, *args, **kwargs)
