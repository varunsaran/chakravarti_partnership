from django.core.management.base import BaseCommand, CommandError
from blog.models import UserData
from blog.models import TransactionHistory
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path
import json
from blog.google_spreadsheet import spreadsheet

import io, urllib, base64
import time
import datetime

class Command(BaseCommand):
    help = 'calls Google Sheets API to fill in TransactionHistory database. One-time script to copy over all data from Google sheets to db.'
    def handle(self, *args, **options):
        sheet = spreadsheet.worksheet("Partner Capital Accounts")
        dates = sheet.col_values(1)
        unit_prices = sheet.col_values(3)
        amounts = sheet.col_values(9)
        users = sheet.col_values(10)

        for i in range(1,430):
            print(i)
            unformatted_date = dates[i]
            if unit_prices[i].__eq__(""):
                transaction_unit_price = 0
            else:
                transaction_unit_price = float(unit_prices[i].replace(",", ""))
            transaction_amount = amounts[i]
            transaction_user = users[i]
            transaction_date = datetime.datetime.strptime(unformatted_date, "%b %d, %Y").date()
            transaction_amount = transaction_amount.strip().replace(",", "")
            if "(" in transaction_amount:
                transaction_amount = transaction_amount.replace("(", "").replace(")", "")
                transaction_amount = transaction_amount.strip()
                transaction_amount = float(transaction_amount)
                transaction_amount *= -1
            if transaction_amount.__eq__(""):
                transaction_amount = 0

            transaction_amount = float(transaction_amount)
            new_transaction = TransactionHistory(sheets_id = transaction_user,
                transaction_amount = transaction_amount,
                unit_price = transaction_unit_price,
                date = transaction_date)
            try:
                new_transaction.save();
            except Exception as e:
                error_msg = f'{e} occured with partner {new_transaction.sheets_id}, amount: {new_transaction.transaction_amount}, date: {new_transaction.date.strftime("%d-%b-%Y")}, row {i})'
                self.stdout.write(error_msg)
                print(error_msg)
