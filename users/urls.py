from  django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_users"),
    path("login", views.login_view, name="login_kr_rha_hu"),
    path("logout", views.logout_view, name="logout_kr_rha_hu")
]