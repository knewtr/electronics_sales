from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("user_create/", UserCreateAPIView.as_view(), name="create"),
    path("user_update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user_delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("user_list/", UserListAPIView.as_view(), name="users_list"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
]
