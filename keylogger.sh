#!/bin/bash  
if [[ $1 == "stop" ]]; then
	python /home/nathan/Projects/linuxlogger/parser.py
	exit
fi
while true
do
	showkey > /home/nathan/Projects/linuxlogger/log.txt
	python /home/nathan/Projects/linuxlogger/parser.py
done
