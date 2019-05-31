 ## Lembretes
- Instalar dependencias.

  `pip install gspread oauth2client`


- Crie uma conta no dataplicity.

- Coloque o supervisor pra rodar após o boot:

  `sudo update-rc.d supervisor defaults`

 - Configure o Raspberry para: 1) aceitar comunicação I2C, 2) inicializar após a rede, 3) dar boot em CLI com usuário pi

 - Abra a crontab:
 
   `sudo crontab -e`
   
 - Adicione o script na crontab:
 
   `@reboot sleep 60 && /home/pi/Documents/raspberry-misc/temperatura-interna-raspberry.py  >> /home/pi/log_crontab.txt`
   
