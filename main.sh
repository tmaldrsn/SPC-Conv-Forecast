#!/bin/bash

#currenttime=$(TZ=GMT date +%H%M)
#echo $currenttime

#TIME=(0105 0605 1205 1305 1635 2005)

#if [[ $TIME == $currenttime ]] then
#		python ./source/lookup_coords.py
#fi

declare -i OUTLOOK
declare -i YEAR
declare -i MONTH
declare -i DAY
declare -i TIME

TIME=1

echo "Enter date (MM/DD/YYYY):"
read date
echo "Enter outlook: (1, 2, 3, or 4):"
read OUTLOOK
while [[ ! $OUTLOOK =~ [1-4] ]]; do
	echo "Not a valid option."
	echo "Enter outlook: (1, 2, 3, or 4):"
	read OUTLOOK
done

if [[ $OUTLOOK = 4 ]]; then
	OUTLOOK=48
fi

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
		echo "The date is not in correct format."
		echo "Enter date (MM/DD/YYYY):"
		read date
	fi
}

while [[ "$condition" = false ]]; do
	checkDate
done

url=`python source/lookup_coords.py $OUTLOOK $YEAR $MONTH $DAY $TIME`
python source/plot_categorical.py $url
