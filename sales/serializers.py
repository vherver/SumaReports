from rest_framework import serializers
from sales.models import Sale

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
