from django.urls import path
from users.views import UserRegisterAPIView


urlpatterns = [path("register/", UserRegisterAPIView.as_view())]
