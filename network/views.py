from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from network.models import Supplier
from network.serializers import SupplierSerializer


class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializers_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        supplier = serializer.save()
        supplier.save()


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializers_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializers_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializers_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)


class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializers_class = SupplierSerializer
    permission_classes = (IsAuthenticated,)
