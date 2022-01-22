#!/usr/bin/env python3
import os
import socket
#import time
from datetime import datetime
import csv
import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# dir_path = os.path.dirname(os.path.realpath(__file__))
# hostname = socket.gethostname()
# # Credenciais do Google Drive API
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(dir_path, 'secret_key.json'), scope)
# client = gspread.authorize(creds)
# # Abre uma o documeto (spreadsheet)
# spreadsheet = client.open(hostname)
# # Abre a planilha (worksheet)
# worksheet = spreadsheet.worksheet('temperatura-cpu')

def conectar():
    # Conectar
    gc = gspread.service_account()
    # Encontrar planilha
    sh = gc.open("arquitetura-responsiva")
    # Encontrar primeira aba
    ws = sh.worksheets()[0]
    return ws



def temperatura():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace('temp=', '').replace("'C\n", ''))



temperatura = float(temperatura())
# data : hora, temperatura
row = [datetime.now().strftime('%d/%m/%Y %H:%M:%-S'), temperatura]
worksheet = conectar()
try :
	worksheet.append_row(row)
except Exception as e:
	print(e)
	print('Erro ao enviar dados para a nuvem')

try:
	with open(os.path.join(dir_path, 'log-temperatura.csv'), 'a') as f:
		w = csv.writer(f)
		w.writerow(row)
except Exception as e:
	print(e)
	print('Erro ao salvar dado em log-temperatura.csv')
