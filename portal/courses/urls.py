from django.urls import path
from . import views
urlpatterns = [
    path('', views.course_list, name='list'),
    path('<str:id>/', views.course_detail,
    name='detail'),
]