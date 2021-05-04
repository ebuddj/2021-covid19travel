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

# Import request for adding headers to our request.
from urllib.request import Request, urlopen

# Read the file and filter columns.
# https://stackoverflow.com/questions/62278538/pd-read-csv-produces-httperror-http-error-403-forbidden/62278737#62278737
url = 'https://reopen.europa.eu/static/changelog.csv'
req = Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
content = urlopen(req)
df = pd.read_csv(content)

df = df[df['LastUpdate'] == '2021-04-29 09:17:00']
df = df[df['Indicator (text in app)'] == 'From within the EU/EEA, may I enter or exit this country for tourism? ']

for index, values  in df.iterrows():
  if (values.value == 'WL'):
    print (values.Country + ': partially https://reopen.europa.eu/en/from-to/DNK/' + values.Country)
  elif (values.value == 'N'):
    print (values.Country + ': no https://reopen.europa.eu/en/from-to/DNK/' + values.Country)
