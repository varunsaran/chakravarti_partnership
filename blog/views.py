from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import UserData
from .models import PartnershipData
from django.contrib.auth.decorators import login_required
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
##GOOGLE SHEETS API IMPORTS
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os.path
import json
from .google_spreadsheet import spreadsheet
# Create your views here.

#OLD HOME FUNCTION
@login_required
def home(request):
    '''scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']    
    BASE = os.path.dirname(os.path.abspath(__file__))
    data = json.loads(open(os.path.join(BASE, "client_secret.json")).read())
    creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1-TxF0p273SPv7XI67SUJCw-oaCxHnYk1CUTRaYJj5Nc/edit#gid=0&fvid=1259069163')
    '''
    sheet = spreadsheet.worksheet("Shareholder Equity")
    partners = sheet.col_values(1)
    amounts = sheet.col_values(3)
    ticker_amounts = {}
    for elem in zip(partners, amounts):
        ticker_amounts[elem[0]] = elem[1]


    starting_deposits = sheet.col_values(9)
    partner_starting_amount = {}
    for elem in zip(partners, starting_deposits):
        partner_starting_amount[elem[0]] = elem[1]


    try:

        #graph partnership change every year + dif in partnership vs S&P500
        sheet = spreadsheet.worksheet("Yearly Performance")
        years = sheet.col_values(1)
        years = years[1:len(years)-1]
        years = list(map(int, years))
        performance = sheet.col_values(2)
        performance = performance[1:len(performance)-1]
        performance = [float(value[:-1]) for value in performance]
        sp500 = sheet.col_values(3)
        sp500 = sp500[1:len(sp500)-1]
        sp500 = [float(value[:-1]) for value in sp500]


        plot = figure(title= 'Partnership vs S&P500' , 
            x_axis_label= 'Year', 
            y_axis_label= 'Performance (%)', 
            plot_width =400,
            plot_height =400)
    except:
        years = [2017,2018,2019]
        performance = [10,10,10]
        sp500 = [10,10,10]

        plot = figure(title= '**TEST graph** check Google Sheet for issues' , 
            x_axis_label= 'Year', 
            y_axis_label= 'Performance (%)', 
            plot_width =400,
            plot_height =400)


    plot.line(years, performance, legend_label= 'partnership', line_width = 2, color='green')
    plot.circle(years, performance, color='green')
    plot.line(years, sp500, legend_label= 'S&P500', line_width = 2, color='orange')
    plot.circle(years, sp500, color='orange')
    #Store components 
    script, div = components(plot)
    
    context = {'ticker_amounts': ticker_amounts, 'partner_starting_amount': partner_starting_amount, 
    'script': script, 'div': div
        }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context )

@login_required
def new_home(request):
    user = request.user
    user_id = user.profile.sheets_id
    user_data = UserData.objects.get(sheets_id=user_id) #pylint: disable=no-member
    year = PartnershipData.objects.values('year') #pylint: disable=no-member
    performance = PartnershipData.objects.values('performance') #pylint: disable=no-member
    sp500 = PartnershipData.objects.values('sp500') #pylint: disable=no-member
    years = [dict['year'] for dict in list(year)]
    performance = [dict['performance'] for dict in list(performance)]
    sp500 = [dict['sp500'] for dict in list(sp500)]
    plot = figure(title= 'Partnership vs S&P500' , 
            x_axis_label= 'Year', 
            y_axis_label= 'Performance (%)', 
            plot_width =400,
            plot_height =400)
    plot.line(years, performance, legend_label= 'partnership', line_width = 2, color='green')
    plot.circle(years, performance, color='green')
    plot.line(years, sp500, legend_label= 'S&P500', line_width = 2, color='orange')
    plot.circle(years, sp500, color='orange')
    script, div = components(plot)

    context = {'title': 'Home', 'user_data': user_data, 'script': script, 'div': div} #pylint: disable=no-member
    return render(request, 'blog/test.html', context )
