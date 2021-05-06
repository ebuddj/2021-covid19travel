#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

#######
# ABOUT
#######

# Covid-19 vaccination data from OWID

########
# AUTHOR
########

# Teemo Tebest (teemo.tebest@gmail.com)

#########
# LICENSE
#########

# CC-BY-SA 4.0 EBU / Teemo Tebest

#######
# USAGE
#######

# python 2021-covid19travel.py

# Load the Pandas libraries with alias pd.
import pandas as pd

# Import xlsxwriter for making Excel files
import xlsxwriter

# Import request for adding headers to our request.
from urllib.request import Request, urlopen

# Import sys for reading arguments.
import sys

# Read the file and filter columns.
import os
if (len(sys.argv) > 1 and sys.argv[1] == 'true'):
  print('\033[1mDownloading latest data\033[0m\n')
  os.system('rm ./data/changelog.csv*')
  os.system('wget https://reopen.europa.eu/static/changelog.csv --directory-prefix=./data/')
else:
  print('\033[1mUsing existing data\033[0m\n')

try:
  df = pd.read_csv('./data/changelog.csv')
except:
  print('Existing data not found, downloading latest data\n')
  os.system('wget https://reopen.europa.eu/static/changelog.csv --directory-prefix=./data/')
  df = pd.read_csv('./data/changelog.csv')

# https://www.kite.com/python/answers/how-to-find-the-max-value-of-a-pandas-dataframe-column-in-python
print('Latest data update is from ' + df['LastUpdate'].max() + '\n')

questions = ['From within the EU/EEA, may I enter or exit this country for tourism? ',
'May I enter this country without a medical certificate or a negative test?',
'May I enter this country by road?',
'Are there any risk areas under lockdown in this country?',
'May I enter this country without being subject to a mandatory quarantine?',
'Restrictions on the provision of tourist services at national or sub-national/regional level']

data = pd.DataFrame(columns=df.columns)

for country in df['Country'].unique():
  for question in questions:
    df_temp_1 = df[(df['Country'] == country) & (df['Indicator (text in app)'] == question)]
    df_temp_2 = df[(df['Country'] == country) & (df['Indicator (text in app)'] == question) & (df['LastUpdate'] == df_temp_1['LastUpdate'].max())]
    
    if df_temp_2.empty == False:
      data = data.append(df_temp_2, ignore_index=True)

data.to_excel('output.xlsx', engine='xlsxwriter')
print('\033[1mDone! Results in output.xlsx\033[0m')

