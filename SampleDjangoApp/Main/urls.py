from django.urls import path
from . import views

from django.conf.urls import include
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'score_log', views.ScoreLogViewSet)

urlpatterns = [

    # router urls
    path('', include(router.urls)),

    # Page Render
    path(r'', views.index, name='index'),

    # APIs
    path(r'get_score', views.GetScore.as_view(), name='score-get')
]