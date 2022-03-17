from rest_framework import serializers
from frontend.models import form


class formSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = "__all__"
