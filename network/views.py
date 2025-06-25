from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from network.models import NetworkLink
from network.serializers import NetworkLinkSerializer
from users.permissions import IsActiveUser


class NetworkLinkCreateAPIView(CreateAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )

    def perform_create(self, serializer):
        supplier = serializer.save()
        supplier.save()


class NetworkLinkRetrieveAPIView(RetrieveAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class NetworkLinkListAPIView(ListAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get("country")
        if country:
            queryset = queryset.filter(contact__country=country)
        return queryset


class NetworkLinkUpdateAPIView(UpdateAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )


class NetworkLinkDestroyAPIView(DestroyAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
    permission_classes = (
        IsAuthenticated,
        IsActiveUser,
    )
