 ## Lembretes
- Instalar dependencias.

  `sudo pip3 install gspread oauth2client`


- Crie uma conta no dataplicity.

- Se tiver problemas em instalar o supervisor, modifique seu /etc/apt/sources.list:

  `deb http://mirrordirector.raspbian.org/raspbian/ stretch main contrib non-free rpi firmware`
  
  `deb http://archive.raspberrypi.org/debian/ stretch main ui`


- Coloque o supervisor pra rodar após o boot:

  `sudo update-rc.d supervisor defaults`

 - Configure o Raspberry para: 
 1) aceitar comunicação I2C
 2) inicializar após a rede
 3) dar boot em CLI com usuário pi
 4) hostname

 - Abra a crontab do usuário pi:
 
   `crontab -e`
   
 - Adicione o script na crontab (a cada 2 minutos):
 
   `*/2 * * * * /home/pi/Documents/raspberry-misc/temperatura-interna-raspberry.py >> /home/pi/log-temp-2-minutos.txt 2>&1`
 
 - [OU] Adicione o script na crontab (ao iniciar):
 
   `@reboot sleep 60 && /home/pi/Documents/raspberry-misc/temperatura-interna-raspberry.py >> /home/pi/log-temp-reboot.txt 2>&1`

