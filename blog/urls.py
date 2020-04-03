from django.urls import path
from . import views

urlpatterns = [
#    path('', views.post_list, name='post_list'),
    path('', views.chart_page, name='chart_page'),
]