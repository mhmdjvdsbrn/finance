from django.db import models

class Service(models.Model):

    SERVICE_CHOICES = [
        ('N', 'Normal'),
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]

    plan_name = models.CharField(max_length=6, choices=SERVICE_CHOICES, default='N')
    price = models.CharField(max_length=12 ,blank=True ,null=True)


    def __str__(self):
        return self.plan_name

