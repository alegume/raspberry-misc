#!/usr/bin/env python3
import os
import time
from datetime import datetime
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

dir_path = os.path.dirname(os.path.realpath(__file__))

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(dir_path, 'secret_key.json'), scope)
client = gspread.authorize(creds)
sheet = client.open('temperatura-raspberry').sheet1

# Return CPU temperature as a character string
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace('temp=', '').replace("'C\n", ''))

while (True):
	temperatura = float(getCPUtemperature())

	# data : hora, temperatura
	row = [datetime.now().strftime('%d/%m/%Y %H:%M:%-S'), temperatura]

	try :
		sheet.append_row(row)
	except:
		print('Erro ao enviar dados para a nuvem')
	try:
		with open('log-temperatura.csv', 'a') as f:
			w = csv.writer(f)
			sheet.append_row(row)
			w.writerow(row)
	except:
		print('Erro ao salvar dado em log-temperatura.csv')
		time.sleep(10)
