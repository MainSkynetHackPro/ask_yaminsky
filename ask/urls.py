from django.conf.urls import url
from .views import AskListView, QuestionView, CreateAskView


urlpatterns = [
    url(
        r'^$',
        AskListView.as_view(),
        name='list'
    ),

    url(
        r'^answer/$',
        QuestionView.as_view(),
        name='list'
    ),

    url(
        r'^ask/$',
        CreateAskView.as_view(),
        name='list'
    )
]