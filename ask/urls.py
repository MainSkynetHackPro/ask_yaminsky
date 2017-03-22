from django.conf.urls import url
from .views import AskListView, QuestionView, CreateAskView, ProfileView, LoginView, RegistrationView

urlpatterns = [
    url(
        r'^$',
        AskListView.as_view(),
        name='list'
    ),

    url(
        r'^answer/$',
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
