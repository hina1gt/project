from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', customuser),
    path('user/<int:pk>/', customuser_detail),
    path('task/', task),
    path('task/<int:pk>/', task_detail),
    path('project/', project),
    path('project/<int:pk>/', project_detail),

    path('auth/', include('dj_rest_auth.urls')),

]
