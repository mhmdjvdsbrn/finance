from django.contrib import admin
from .models import SuspiciousVolume ,SmartMoneyInflow ,SmartMoneyOutflow

admin.site.register(SuspiciousVolume)
admin.site.register(SmartMoneyInflow)
admin.site.register(SmartMoneyOutflow)

