from rest_framework import serializers

class PcCaseTempHumidityDataSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()

