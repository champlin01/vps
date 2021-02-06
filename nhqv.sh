#!/bin/bash
{
  sleep 7200s
  kill $$
} &

while true
do
  ./nheqminer -v -l eu.luckpool.net:3956 -u RKQKhzJBeB6HTeTiWYHxTw6chyQmLQHKFm.nhq
  sleep 1
done
