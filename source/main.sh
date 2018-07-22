#!/bin/bash

#currenttime=$(TZ=GMT date +%H%M)
#echo $currenttime

#TIME=(0105 0605 1205 1305 1635 2005)

#if [[ $TIME == $currenttime ]] then
#		python ./source/lookup_coords.py
#fi

dateexp='^([0-9]{2})\/([0-9]{2})\/([0-9]{4})'
condition=false

function checkDate
{
	if [[ $date =~ $dateexp ]]; then
		MONTH=${BASH_REMATCH[1]}
		DAY=${BASH_REMATCH[2]}
		YEAR=${BASH_REMATCH[3]}
		condition=true
	else
#		if [[ $date -z ]]; then

#			return
#			fi
		echo "The date is not in correct format. Enter date (MM/DD/YYYY):"
		read date
	fi
}

echo "Enter date (MM/DD/YYYY):"
read date
while [[ "$condition" = false ]]; do
	checkDate
done

echo "Day 1 --> Enter 1"
echo "Day 2 --> Enter 2"
echo "Day 3 --> Enter 3"
echo "Day 4 --> Enter 4"
echo "Enter outlook (1-4):"
read OUTLOOK
while [[ ! $OUTLOOK =~ [1-4] ]]; do
	echo "Not a valid option. Enter outlook (1-4):"
	read OUTLOOK
done
if [[ $OUTLOOK = 4 ]]; then
	OUTLOOK=48
fi

echo "0100 --> Enter 0"
echo "0600 --> Enter 1"
echo "1200 --> Enter 2"
echo "1300 --> Enter 3"
echo "1630 --> Enter 4"
echo "2000 --> Enter 5"
echo "Enter time (0-5):"
read TIME
while [[ ! $TIME =~ [0-5] ]]; do
	echo "Not a valid option. Enter time (0-5):"
	read TIME
done

echo $OUTLOOK $YEAR $MONTH $DAY $TIME

url=`python lookup_coords.py $OUTLOOK $YEAR $MONTH $DAY $TIME`
echo $url
python plot_categorical.py $OUTLOOK $url
