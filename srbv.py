import os,sys
from time import sleep

waktu = 1

while True:
	try:
		waktu =+ 1
		if waktu == 5:
			os.system("./srb --disable-gpu --algorithm verushash --pool stratum+tcp://eu.luckpool.net:3956 --wallet RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.p1")
			waktu = 1
		else:
			print("Wait ... "+str(waktu))
		sleep(1)
	except Exception as e:
		print(e)
