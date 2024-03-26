#!/bin/bash

day=$(date +%d)
month=$(date +%m)
year=$(date +%Y)
hour=$(date +%H)
minute=$(date +%M)
second=$(date +%S)


cp /var/log/syslog .
echo "Orginal  syslog file before append:"
cat syslog 


echo "Today date: $month-$day-$year" >> syslog
echo "Today time: $hour:$minute:$second" >> syslog
echo "Appended file:"
cat syslog