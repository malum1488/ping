import os
import telethon

api_id = "1434664"
api_hash = "22c3adcb3fe515a49103ffa229e1ecd2"

client = TelegramClient('Telethon', api_id, api_hash)
client.start()



hostname = ['192.168.10.1','192.168.10.2','8.8.8.8']
while True:

	for i in hostname:
		response = os.system("ping -c 1 " + i)

		if response == 0:
	  		print('is up))')
	  		client.send_message('user', 'Vse Pizda upal ' + i)
		else:
			client.send_message('user', 'Vse Pizda upal ' + i)
	  		print('is down((')
	  		os.system('rasdial.exe "Juk" "Juck" "ASD3412(123kSAJD12312&$*@*&#$Hsad"')
	  		os.system('rasdial.exe "K2" "Kiev2" JAK123jJA*@!&jJSADJKMjsdnm12lqwikJA*@#B"')
	  		os.system('rasdial.exe "smallOfice" "pppcamera" "Jhj23812j&^!JksadosakKJHS2139(*&^!@#$SAFD11"')
	  		chack = os.system("ping -c 1 " + i)
	  		if chack == 0:
	  			os.system('route add 192.168.95.0 mask 255.255.255.0 14.10.10.1')
	  			os.system('route add 192.168.85.0 mask 255.255.255.0 16.10.10.1')
	  			os.system('route add 192.168.15.0 mask 255.255.255.0 12.10.10.1')


