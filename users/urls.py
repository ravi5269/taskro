from django.urls import path
from users.views import UserRegisterAPIView
from users.views import UserAPIView


urlpatterns = [
    path("register/", UserRegisterAPIView.as_view()),
    path("register/<int:pk>", UserRegisterAPIView.as_view(), name="user"),
    path("user/", UserAPIView.as_view()),
    path("user/<int:pk>", UserAPIView.as_view())
]
