# from django.urls import path
# from .import views

# # Create your URLs here..!
# urlpatterns = [
#     path("login/",views.login_view,
#          name = "login")
# ]


from django.urls import path
from . import views

urlpatterns = [

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

]