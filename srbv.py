import os,sys

waktu = 1

while True:
	waktu =+ 1
	if waktu == 5:
		os.system("./srb --disable-gpu --algorithm verushash --pool stratum+tcp://eu.luckpool.net:3956 --wallet RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.p1")
		waktu = 1
	else:
		print("Wait ...")
