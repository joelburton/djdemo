from django.conf.urls import url

from todo import views

urlpatterns = [
    url(r'^$', views.TaskListListView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.TaskListDetailView.as_view()),
]
