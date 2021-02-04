import os,sys
from time import sleep
import schedule

def run():
	os.system("./srb --disable-gpu --algorithm verushash --pool stratum+tcp://eu.luckpool.net:3956 --wallet RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.p1")

schedule.every(5).seconds.do(run)
#schedule.every(10).minutes.do(run)

while True:
	schedule.run_pending()
	sleep(1)
