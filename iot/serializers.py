from rest_framework import serializers

class PcCaseTempHumidityDataSerializer(serializers.Serializer):
    temperature = serializers.FloatField(allow_null=True, required=False)
    humidity = serializers.FloatField(allow_null=True, required=False)
    last_posted_time = serializers.DateTimeField(allow_null=True, required=False)
    status = serializers.CharField(max_length=20, default='offline')


