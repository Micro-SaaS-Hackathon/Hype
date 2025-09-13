from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('statistics/<str:category>/', views.statistics, name='statistics'),
    path("news/", views.news, name="news"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("team/", views.team, name="team"),
    path("analyse/<str:category>/", views.analyse, name="analyse")
]