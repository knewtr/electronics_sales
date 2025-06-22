from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from network.models import NetworkLink


class NetworkLinkSerializer(ModelSerializer):
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = NetworkLink
        fields = ("name", "type", "product", "supplier", "debt")
