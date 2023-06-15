from django.urls import path
from tasks.views import TaskAPIView, SubTaskAPIView


urlpatterns = [
    path("task/", TaskAPIView.as_view()),
    path("task/<int:pk>", TaskAPIView.as_view()),
    path("subtask/", SubTaskAPIView.as_view()),
    path("subtask/<int:pk>", SubTaskAPIView.as_view()),
]
