from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('projects/<int:pk>/',views.Progect_Detail_View.as_view(),name='project_detail',
    ),
]