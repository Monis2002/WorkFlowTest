from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
    path('all_clear/', all_clear, name='all_clear'),
    path('edit/<int:task_id>',task_edit,name='task_edit')
]
