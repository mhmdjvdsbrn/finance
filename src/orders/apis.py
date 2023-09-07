from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.db import transaction
from drf_spectacular.utils import extend_schema
from .models import Order 
from services.models import Service
from .services import create_order 
from .selectors import order_detail 
from users.mixins import ApiAuthMixin
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime


class ServicesDetail(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("plan_name" , "price")
        
class BuyPlanApi(APIView):
    permission_classes = [IsAuthenticated] 

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ["service"]

    class OutPutSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField("get_user")
        service = ServicesDetail(read_only=True)
        class Meta:
            model = Order
            fields = ("pay_time", "start_time", "end_time" ,"user" ,"service")

        def get_user(self, order):
            return order.user.email

    @extend_schema(
        responses=OutPutSerializer,
        request=InputSerializer,
    )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_order(
                user=request.user,
                service=serializer.validated_data.get("service"),
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(self.OutPutSerializer(query, context={"request":request}).data)


class DetailOrderApi(APIView):
    permission_classes = [IsAuthenticated] 

            
    class OutPutDetailSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField("get_user")
        service = ServicesDetail(read_only=True)
        remainingـperiod = serializers.SerializerMethodField("get_period")
        class Meta:
            model = Order
            fields = ("order_id","pay_time", "start_time", "end_time" , "remainingـperiod" ,"is_active","user" ,"service")

        def get_user(self, order):
            return order.user.email

        def get_period(self ,order):
            end_time = str(order.end_time)
            time_now =str(timezone.now())
            date1 = datetime.fromisoformat(end_time)
            date2 = datetime.fromisoformat(time_now)
            time_difference = date1 - date2
            days_remaining = time_difference.days
            if days_remaining != '0':
                order.is_active = True
            else:
                order.is_active = False
            return days_remaining

        def get_user(self, order):
            return order.user.email
    @extend_schema(
        responses=OutPutDetailSerializer,
    )
    def get(self, request):
        try:
            query = order_detail(user=request.user)
        except Exception as ex:
            return Response(
                {"detail": "Not Found -- " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.OutPutDetailSerializer(query)

        return Response(serializer.data) 

class UpdateOrderApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ["service"]

    class OutPutUpdateSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField("get_user")
        service = ServicesDetail(read_only=True)

        class Meta:
            model = Order
            fields = ("pk", "order_id", "pay_time", "start_time", "end_time", "user", "service")

        def get_user(self, order):
            return order.user.email

    @extend_schema(
        request=InputUpdateSerializer,
        responses=OutPutUpdateSerializer,
    )
    def put(self, request, order_id):
        serializer = self.InputUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                order = Order.objects.get(pk=order_id)
                order.service = serializer.validated_data.get("service")
                order.save()
            updated_order = Order.objects.get(pk=order_id)

        except Order.DoesNotExist:
            return Response(
                {"detail": "Order not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(self.OutPutUpdateSerializer(updated_order).data)



