from django.conf.urls import url
from .views import (
    ArticleAddView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
)
from . import views


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='articles_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^add/$', ArticleAddView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleUpdateView.as_view(), name='edit'),
    url(r'^email/$', views.email, name='contact'),
]
