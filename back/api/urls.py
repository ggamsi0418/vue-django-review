from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    # auth
    # CRUD
    path('post/create/', views.ApiPostCV.as_view(), name='post_create'),
]
