# workflow/urls.py
from django.urls import include, path, url
from rest_framework import routers
from . import views


app_name = 'workflowapp'

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^workflow/$', views.workflowListView.as_view()),
    url(r'^comment/$', views.commentListView.as_view()),
    url(r'^workflow/(?P<pk>[0-9]+)$', views.workflowViewSet.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)$', views.commentViewSet.as_view()),
    url(r'^step/(?P<pk>[0-9]+)$', views.stepViewSet.as_view())
]
