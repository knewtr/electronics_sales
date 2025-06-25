from django.urls import path

from network.apps import NetworkConfig
from network.views import (NetworkLinkCreateAPIView, NetworkLinkDestroyAPIView,
                           NetworkLinkListAPIView, NetworkLinkRetrieveAPIView,
                           NetworkLinkUpdateAPIView)

app_name = NetworkConfig.name

urlpatterns = [
    path("link/create/", NetworkLinkCreateAPIView.as_view(), name="link_create"),
    path("link/list/", NetworkLinkListAPIView.as_view(), name="link_list"),
    path(
        "link/<int:pk>/",
        NetworkLinkRetrieveAPIView.as_view(),
        name="link_retrieve",
    ),
    path(
        "link/update/<int:pk>/", NetworkLinkUpdateAPIView.as_view(), name="link_update"
    ),
    path("link/delete/", NetworkLinkDestroyAPIView.as_view(), name="link_delete"),
]
