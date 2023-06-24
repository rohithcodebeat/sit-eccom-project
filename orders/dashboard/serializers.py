from ..models import OrderModel
from rest_framework import serializers 


class DashboardOrderModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ["status"]
    


