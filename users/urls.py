from django.urls import include, path
from .views import UserListView, PostViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('post', PostViewSet)

urlpatterns = [
    path('',UserListView.as_view()),
    path('',include(routers.urls))
]