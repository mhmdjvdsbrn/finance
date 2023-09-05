from django.db import models

class Service(models.Model):

    SERVICE_CHOICES = [
        ('N', 'Normal'),
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]

    plan_name = models.CharField(max_length=6, choices=SERVICE_CHOICES, default='N')
    price_monthly_gold = models.CharField(max_length=12 ,blank=True ,null=True)
    price_monthly_silver = models.CharField(max_length=12 ,blank=True ,null=True)
    price_monthly_bronze = models.CharField(max_length=12 ,blank=True ,null=True)
    price_free_normal = models.CharField(max_length=12 ,blank=True ,null=True)

    def __str__(self):
        return self.plan_name

