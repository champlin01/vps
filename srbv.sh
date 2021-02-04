#!/bin/sh
while [ true ]
do
    timeout 60 bash -c -- 'while true; do ./srbc.sh;done'
done
