from rest_framework import serializers
from .models import ScrapModel

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapModel
        fields = "__all__"
