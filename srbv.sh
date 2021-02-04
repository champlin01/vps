#!/bin/bash
START='date +%s'
while [ $(( $(date +%s) - 60 )) -lt $START ]; do
  ./srb --disable-gpu --algorithm verushash --pool stratum+tcp://eu.luckpool.net:3956 --wallet RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.p1
done
