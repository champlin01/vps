#!/bin/bash
{
  sleep 7200s
  kill $$
} &

while true
do
  ./srb --disable-gpu --algorithm verushash --pool stratum+tcp://eu.luckpool.net:3956 --wallet RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.p1
  sleep 1
done
