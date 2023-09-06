from django.db import models
from django.contrib.auth import get_user_model
from services.models import Service
from django.db.models.query import F, Q
from datetime import timedelta
from django.utils import timezone

User = get_user_model()


class CheckStartedEnded(models.Model):
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.start_time:
            self.start_time = timezone.now()
        if not self.end_time:
            self.end_time = self.start_time + timedelta(days=31)
        super(CheckStartedEnded, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        constraints = [
            models.CheckConstraint(
                name="start_date_before_end_time",
                check=Q(start_time__lt=F("end_time"))
            )
        ]

class Order(CheckStartedEnded):
    order_id = models.IntegerField(primary_key=True ,blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True ,related_name="user")
    service = models.ForeignKey(Service , on_delete=models.CASCADE ,related_name="service")
    pay_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email




