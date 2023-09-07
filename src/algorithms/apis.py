from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from django.utils import timezone
from django.db import transaction
from .models import SuspiciousVolume
from .permission import HasSuspiciousView
from .selectors import show_suspicious_volume

from datetime import datetime




class SuspiciousVolumeUserApi(APIView):
    permission_classes = [IsAuthenticated ,HasSuspiciousView ] 
    class OutPutVolumeSerializer(serializers.ModelSerializer):

        class Meta:
            model = SuspiciousVolume
            fields = ['j_date' ,'date' ,'weekday' ,'volume' ,'ticker' ,'name' ,'market']

    @extend_schema(
        responses=OutPutVolumeSerializer,
    )
    def get(self, request):
        try:
            volume = SuspiciousVolume.objects.order_by('-j_date')
        except Exception as ex:
            return Response(
                {"detail": "Not Found -- " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutVolumeSerializer(volume  ,many=True)
        return Response(serializer.data) 