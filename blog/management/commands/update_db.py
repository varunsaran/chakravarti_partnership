from django.core.management.base import BaseCommand, CommandError
from blog.models import UserData

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path
import json
from blog.google_spreadsheet import spreadsheet

class Command(BaseCommand):
    help = 'calls Google Sheets API to update app database with up-to-date user data'
    def handle(self, *args, **options):
        #self.stdout.write('test')
        ''' data = UserData.objects.get(sheets_id="VS") #pylint: disable=no-member
        data.estimated_annual_income = 50
        data.save()'''

        sheet = spreadsheet.worksheet("Shareholder Equity")
        partners = sheet.col_values(1)
        shareholder_equity = sheet.col_values(3)

        for elem in zip(partners, shareholder_equity):
            try:
                partner_obj = UserData.objects.get(sheets_id=elem[0]) #pylint: disable=no-member
                partner_equity = elem[1]
                if partner_equity[0] == '$':
                    partner_equity = partner_equity[1:]
                partner_obj.current_equity = int(partner_equity.replace(',', ''))
                partner_obj.save()
            except Exception as e:
                error_msg = f'{e} occured with partner {elem[0]} '
                self.stdout.write(error_msg)

        equity_deposits = sheet.col_values(9)
        for elem in zip(partners, equity_deposits):
            try:
                partner_obj = UserData.objects.get(sheets_id=elem[0]) #pylint: disable=no-member
                partner_deposit = elem[1]
                if partner_deposit[0] == '$':
                    partner_deposit= partner_deposit[1:]
                partner_obj.net_equity_deposit = round(float(partner_deposit.replace(',', '')))
                partner_obj.save()
            except Exception as e:
                error_msg = f'{e} occured with partner {elem[0]} '
                self.stdout.write(error_msg)

        est_incomes = sheet.col_values(6)
        for elem in zip(partners, est_incomes):
            try:
                partner_obj = UserData.objects.get(sheets_id=elem[0]) #pylint: disable=no-member
                partner_income = elem[1]
                if partner_income[0] == '$':
                    partner_income= partner_income[1:]
                partner_obj.estimated_annual_income = round(float(partner_income.replace(',', '')))
                partner_obj.save()
            except Exception as e:
                error_msg = f'{e} occured with partner {elem[0]} '
                self.stdout.write(error_msg)

        ownership_percents = sheet.col_values(8)
        for elem in zip(partners, ownership_percents):
            try:
                partner_obj = UserData.objects.get(sheets_id=elem[0]) #pylint: disable=no-member
                ownership_percent = elem[1]
                if ownership_percent[-1] == '%':
                    ownership_percent= float(ownership_percent[:-1]) / 100
                else:
                    ownership_percent= float(ownership_percent) / 100
                partner_obj.percentage_ownership = ownership_percent
                partner_obj.save()
            except Exception as e:
                error_msg = f'{e} occured with partner {elem[0]} '
                self.stdout.write(error_msg)
        
        metrics_sheet = spreadsheet.worksheet("Metrics")
        partnership_days_gain = metrics_sheet.acell('B9').value
        partnership_days_gain = partnership_days_gain.replace('$', '')
        partnership_days_gain = float(partnership_days_gain.replace(',', ''))
        for partner_obj in UserData.objects.all():  #pylint: disable=no-member
            try:
                partner_obj.daily_gain = partnership_days_gain * partner_obj.percentage_ownership
                partner_obj.save()
                msg = str(partner_obj.daily_gain)
                self.stdout.write(msg)

            except Exception as e:
                error_msg = f'{e} occured with partner {elem[0]} '
                self.stdout.write(error_msg)


        
        
        
        





        