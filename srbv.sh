#!/bin/sh
while [ true ]
do
    timeout 5 bash -c -- 'while true; do ./srbc.sh;done'
done
