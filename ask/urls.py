from django.conf.urls import url
from .views import AskListView, TopAskListView, QuestionView, CreateAskView, ProfileView, LoginView, RegistrationView, ByTagView

urlpatterns = [
    url(
        r'^$',
        AskListView.as_view(),
        name='list'
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
        r'^registration/$',
        RegistrationView.as_view(),
        name='registration'
    )
]
