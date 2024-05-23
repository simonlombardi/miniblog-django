from django.urls import path

from home.views import (
    index_view,
    Login_view,
    Logout_view,
)

urlpatterns = [
    path(route="", view = index_view, name = "index"),
    path(route="login/", view=Login_view.as_view(), name="login"),
    path(route="logout/", view=Logout_view.as_view(), name="logout")


]