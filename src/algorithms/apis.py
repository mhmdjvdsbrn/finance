from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from django.utils import timezone
from django.db import transaction
from .models import SuspiciousVolume ,SmartMoneyInflow ,SmartMoneyOutflow
from .permission import HasSuspiciousView ,HasSmartMoneyInflowView ,HasSmartMoneyOutflowView
from .selectors import show_suspicious_volume ,show_smart_money_inflow ,show_smart_money_outflow

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
            volume = show_suspicious_volume()
        except Exception as ex:
            return Response(
                {"detail": "Not Found -- " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutVolumeSerializer(volume  ,many=True)
        return Response(serializer.data) 




class SmartMoneyInflowApi(APIView):
    permission_classes = [IsAuthenticated ,HasSmartMoneyInflowView] 
    class OutPutInflowSerializer(serializers.ModelSerializer):

        class Meta:
            model = SmartMoneyInflow
            fields = ['j_date' ,'ticker' ,'name' ,'market']

    @extend_schema(
        responses=OutPutInflowSerializer,
    )
    def get(self, request):
        try:
            volume = show_smart_money_inflow()
        except Exception as ex:
            return Response(
                {"detail": "Not Found -- " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutInflowSerializer(volume  ,many=True)
        return Response(serializer.data) 


class SmartMoneyOutflowApi(APIView):
    permission_classes = [IsAuthenticated ,HasSmartMoneyOutflowView] 
    class OutPutOutflowSerializer(serializers.ModelSerializer):

        class Meta:
            model = SmartMoneyOutflow
            fields = ['j_date' ,'ticker' ,'name' ,'market']
    @extend_schema(
        responses=OutPutOutflowSerializer,
    )
    def get(self, request):
        try:
            volume = show_smart_money_outflow()
        except Exception as ex:
            return Response(
                {"detail": "Not Found -- " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutOutflowSerializer(volume  ,many=True)
        return Response(serializer.data) 