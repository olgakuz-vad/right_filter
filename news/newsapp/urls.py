from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='search'),

]