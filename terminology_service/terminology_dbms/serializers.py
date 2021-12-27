from rest_framework import serializers

from .models import Directory, DirectoryItem


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ['name', 'short_name', 'description', 'version', 'start_date']


class DirectoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectoryItem
        fields = ['directory', 'parent', 'code', 'value']
