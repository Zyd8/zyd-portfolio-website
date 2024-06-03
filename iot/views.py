from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PcCaseTempHumidityDataSerializer
from django.shortcuts import render


def iot(request):
    return render(request, "iot.html")


current_data = {'temperature': None, 'humidity': None}
@api_view(['POST'])
def post_pc_case_temp_humidity(request):
    serializer = PcCaseTempHumidityDataSerializer(data=request.data)
    if serializer.is_valid():
        global current_data
        current_data['temperature'] = serializer.validated_data['temperature']
        current_data['humidity'] = serializer.validated_data['humidity']
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pc_case_temp_humidity(request):
    return render(request, 'iot.html', current_data)
