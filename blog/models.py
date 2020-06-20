from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    sheets_id = models.CharField(max_length=15, unique=True)
    current_equity = models.IntegerField()
    net_equity_deposit = models.IntegerField()
    estimated_annual_income = models.IntegerField()
    percentage_ownership = models.FloatField(default = 0.0)
    daily_gain = models.FloatField(default = 0.0)


    def __str__(self):
        return f'Data for {self.sheets_id}'

class PartnershipData(models.Model):
    year = models.IntegerField(unique=True)
    performance = models.FloatField()
    sp500 = models.FloatField()

    def __str__(self):
        return f'Performance data for year {self.year}'

class TransactionHistory(models.Model):
    sheets_id = models.CharField(max_length=15)
    transaction_amount = models.FloatField()
    unit_price = models.FloatField()
    date = models.DateTimeField()
    def __str__(self):
        return f'Transaction on {self.date} by {self.sheets_id} for ${self.transaction_amount}'
