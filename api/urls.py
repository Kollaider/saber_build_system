from django.urls import path
from .views import TaskView

urlpatterns = [
    path('get_tasks/', TaskView.as_view(), name='get-tasks'),
]
