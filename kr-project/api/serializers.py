from rest_framework import serializers


class FindDomainSerializer(serializers.Serializer):
    text = serializers.CharField(min_length = 4)
    result = serializers.CharField()
    