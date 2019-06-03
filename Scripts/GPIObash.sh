#!/bin/bash
counter=1
gpio mode 0 out
gpio mode 1 out
while [ $counter -le 10 ]

do
	gpio write 0 1
	gpio write 1 1
	echo "both on"
	sleep 1
	((counter ++))
	gpio write 0 0
	gpio write 1 0
	echo "both off"
	sleep 1
done
echo "hi"
