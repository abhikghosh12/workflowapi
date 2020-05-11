# workflow/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
app_name = 'workflowapp'

router = routers.DefaultRouter()
#router.register(r'workflow',views.workflowViewSet)
#router.register(r'comment', views.commentViewSet)
#router.register(r'steps', views.stepViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('workflow/(?P<pk>[0-9]+)', views.workflowViewSet.as_view(), name="workflow"),
    url(r'^workflow/(?P<pk>[0-9]+)$', views.workflowViewSet.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)$', views.commentViewSet.as_view()),
    url(r'^step/(?P<pk>[0-9]+)$', views.stepViewSet.as_view())
    #path('comment/(?P<pk>[0-9]+)', views.commentViewSet.as_view(), name="comment"),
    #path('step/(?P<pk>[0-9]+)', views.stepViewSet.as_view(), name="step")
]
