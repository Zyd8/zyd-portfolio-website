from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PcCaseTempHumidityDataSerializer
from django.http import JsonResponse
from datetime import datetime, timedelta


current_data = {'temperature': None, 'humidity': None, 'last_posted_time': None, 'status': None}

def iot(request):
    return render(request, "iot.html", {'current_data': current_data})

@api_view(['POST'])
def post_pc_case_temp_humidity(request):
    serializer = PcCaseTempHumidityDataSerializer(data=request.data)
    if serializer.is_valid():
        global current_data
        current_data['temperature'] = serializer.validated_data['temperature']
        current_data['humidity'] = serializer.validated_data['humidity']
        current_data['last_posted_time'] = datetime.now().isoformat()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_current_data(request):

    if current_data['last_posted_time']:
        last_posted_time = datetime.fromisoformat(current_data['last_posted_time'])
        if datetime.now() - last_posted_time > timedelta(minutes=2):

            current_data['status'] = 'offline'
            current_data['temperature'] = None
            current_data['humidity'] = None

        else:
            current_data['status'] = 'online'
    else:
        current_data['status'] = 'offline'
        current_data['temperature'] = None
        current_data['humidity'] = None

    return JsonResponse(current_data)

