from django.db import models



class SuspiciousVolume(models.Model):
    j_date = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    weekday = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    market = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.ticker} {self.j_date}'

class SmartMoneyInflow(models.Model):
    j_date = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    market = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ticker} {self.j_date}'

class SmartMoneyOutflow(models.Model):
    j_date = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    market = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ticker} {self.j_date}'