from django.urls import path
from . import views

urlpatterns = [
path("", views.Index.as_view(),name="index-one"),
path("club-single", views.ClubSingle.as_view(),name="club-single"),
path("registration", views.Clubreg.as_view(),name="registration"),
#path("dashboard", views.Dashboard.as_view(),name="dashboard"),
path("payment", views.Payment.as_view(),name="payment"),
path("club/<int:id>",views.ClubSingle.as_view(),name="single-club"),
#path("login", views.Login.as_view(),name="login"),
]