from django.urls import path
from . import views

urlpatterns = [

    # Page Render,
    path(r'', views.index, name='index'),

    # APIs
    path(r'get_score', views.GetScore.as_view(), name='score-get')
]