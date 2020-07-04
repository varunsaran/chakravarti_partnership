from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Defines all databases as models, in a class-like structure. Defines all db columns, and their types

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
class Holdings(models.Model):
    ticker = models.CharField(unique=True, max_length=40)
    position_size = models.FloatField()
    category = models.CharField(max_length=60)
    quantity = models.FloatField()
    price = models.FloatField()
    change_pct = models.FloatField()
    change = models.FloatField()
    todays_gain = models.FloatField()
    overall_gain = models.FloatField()
    overall_pct_gain = models.FloatField()
    div_per_share = models.FloatField()
    income_pct = models.FloatField()
    dividend = models.FloatField()
    volume = models.FloatField()
    volume_avg = models.FloatField()
    def __str__(self):
        return f'Info for Ticker {self.ticker}'
