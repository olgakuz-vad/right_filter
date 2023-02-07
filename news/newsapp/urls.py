from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('<slug:post_slug>/', PostDetail.as_view(), name='post'),
]