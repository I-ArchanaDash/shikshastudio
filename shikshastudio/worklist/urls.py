from django.urls import path
from .views import TaskList, TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CostumLoginView,RegisterPage

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',RegisterPage.as_view(),name='register'),
    path('login/',CostumLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='http://localhost:8000'),name='logout'),
    path('teacher-worklist/',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task-delete'),
]