from django.core.management.base import BaseCommand, CommandError
from blog.models import UserData
from blog.models import Holdings
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path
import json
from blog.google_spreadsheet import spreadsheet

import io, urllib, base64
import time
import datetime

# Gathers all holdings data from the Google Sheets, and copies over to Django db.
class Command(BaseCommand):
    help = 'calls Google Sheets API to fill in TransactionHistory database. One-time script to copy over all data from Google sheets to db.'
    def handle(self, *args, **options):
        sheet = spreadsheet.worksheet("Holdings")
        first_row = sheet.row_values(1)

        ticker_index = first_row.index("Ticker") + 1
        tickers = sheet.col_values(ticker_index)[1:]

        size_index = first_row.index("Position Size") + 1
        position_sizes = sheet.col_values(size_index)[1:]

        category_index = first_row.index("Category") + 1
        categories = sheet.col_values(category_index)[1:]

        quantity_index = first_row.index("Quantity") + 1
        quantities = sheet.col_values(quantity_index)[1:]

        price_index = first_row.index("Price") + 1
        prices = sheet.col_values(price_index)[1:]

        change_pct_index = first_row.index("ChangePct") + 1
        change_pcts = sheet.col_values(change_pct_index)[1:]

        change_index = first_row.index("Change") + 1
        changes = sheet.col_values(change_index)[1:]

        todays_gain_index = first_row.index("Today's Gain") + 1
        todays_gains = sheet.col_values(todays_gain_index)[1:]

        overall_gain_index = first_row.index("Overall Gain") + 1
        overall_gains = sheet.col_values(overall_gain_index)[1:]

        overall_pct_gain_index = first_row.index("Overall Pct Gain") + 1
        overall_pct_gains = sheet.col_values(overall_pct_gain_index)[1:]

        div_per_share_index = first_row.index("Div/Shr") + 1
        div_per_shares = sheet.col_values(div_per_share_index)[1:]

        income_pct_index = first_row.index("Income Percentage") + 1
        income_pcts = sheet.col_values(income_pct_index)[1:]

        dividend_index = first_row.index("Dividend") + 1
        dividends = sheet.col_values(dividend_index)[1:]

        volume_index = first_row.index("Volume") + 1
        volumes = sheet.col_values(volume_index)[1:]

        volume_avg_index = first_row.index("VolumeAvg") + 1
        volume_avgs = sheet.col_values(volume_avg_index)[1:]




        for i in range(0,len(tickers)):
            try:
                ticker= tickers[i]
                size = float(position_sizes[i].replace("$", "").replace(",", ""))
                category = categories[i]
                quantity = float(quantities[i].replace(",", "").replace("$", ""))
                price = float(prices[i].replace("$", "").replace(",", ""))
                change_pct = float(change_pcts[i].replace("%", "").replace(",", ""))/100
                change = float(changes[i].replace("$", "").replace(",", ""))
                todays_gain = float(todays_gains[i].replace("$", "").replace(",", ""))
                overall_gain = float(overall_gains[i].replace("$", "").replace(",", ""))
                overall_pct_gain = float(overall_pct_gains[i].replace("%", "").replace(",", ""))/100
                if div_per_shares[i]=='':
                    div_per_share = 0
                else:
                    div_per_share = float(div_per_shares[i].replace("$", "").replace(",", ""))
                income_pct = float(income_pcts[i].replace("%", "").replace(",", ""))/100
                dividend = float(dividends[i].replace("$", "").replace(",", ""))
                volume = float(volumes[i].replace(",", ""))
                if volume_avgs[i]=='#N/A':
                     volume_avg = 0
                else:
                    volume_avg = float(volume_avgs[i].replace(",", ""))

                new_holding = Holdings(ticker=ticker, position_size=size, category=category, quantity=quantity, price=price,
                change_pct=change_pct, change=change, todays_gain=todays_gain, overall_gain=overall_gain,overall_pct_gain=overall_pct_gain,
                div_per_share=div_per_share, income_pct=income_pct, dividend=dividend, volume=volume, volume_avg=volume_avg)

                new_holding.save();
            except Exception as e:
                error_msg = f'{e} occured with ticker {ticker}'
                print("**************************************########################********************")
                print(error_msg)
                print("**************************************########################*********************")
