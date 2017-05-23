from django.conf.urls import url
from .views import AskListView, TopAskListView, QuestionView, CreateAskView, ProfileView, LoginView, RegistrationView, \
    ByTagView, logout_view, vote_ask, vote_answer, mark_answer, asks_autocomplete

urlpatterns = [

    url(
        r'^autocomplete/asks/$',
        asks_autocomplete,
        name='autocomplete_asks'
    ),

    url(
        r'^$',
        AskListView.as_view(),
        name='list'
    ),

    url(
        r'^vote/ask/$',
        vote_ask,
        name='vote_ask'
    ),

    url(
        r'^vote/answer/$',
        vote_answer,
        name='vote_answer'
    ),

    url(
        r'^mark/answer/$',
        mark_answer,
        name='mark_answer'
    ),

    url(
        r'^(?P<page>[0-9]+)/$',
        AskListView.as_view(),
        name='list'
    ),

    url(
        r'^top/$',
        TopAskListView.as_view(),
        name='top_list'
    ),

    url(
        r'^top/(?P<page>[0-9]+)/$',
        TopAskListView.as_view(),
        name='top_list'
    ),

    url(
        r'^tag/(?P<pk>[0-9]+)/$',
        ByTagView.as_view(),
        name='tag_view'
    ),

    url(
        r'^tag/(?P<pk>[0-9]+)/(?P<page>[0-9]+)$',
        ByTagView.as_view(),
        name='tag_view'
    ),

    url(
        r'^answer/(?P<pk>\w+)$',
        QuestionView.as_view(),
        name='show'
    ),

    url(
        r'^ask/$',
        CreateAskView.as_view(),
        name='ask'
    ),

    url(
        r'^profile/$',
        ProfileView.as_view(),
        name='profile'
    ),

    url(
        r'^login/$',
        LoginView.as_view(),
        name='login'
    ),

    url(
        r'^logout/$',
        logout_view,
        name='logout'
    ),

    url(
        r'^registration/$',
        RegistrationView.as_view(),
        name='registration'
    )
]
