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
		echo "The date is not in correct format. Enter date (MM/DD/YYYY):"
		read date
	fi
}

function checkForecast
{
  if [[ ! $OUTLOOK =~ [1-4] ]]; then
    echo "|==========================|"
    echo "|     Choose Day Outlook   |"
    echo "|==========================|"
    echo "|     Day 1 --> Enter 1    |"
    echo "|     Day 2 --> Enter 2    |"
    echo "|     Day 3 --> Enter 3    |"
    echo "|  Days 4-8 --> Enter 4    |"
    echo "|==========================|"
    read -p "Enter outlook (1-4): " OUTLOOK
  else
    if [ $OUTLOOK -eq 3 ]; then
      $TIME="0730"
    fi
    echo "Invalid option, please choose an outlook"
  fi
}

function checkTime
{
  if [ $OUTLOOK == 1 ]; then
    echo "|===============================|"
    echo "|  Choose Outlook Time (DAY 1)  |"
    echo "|===============================|"
    echo "|       0100Z --> Enter 1       |"
    echo "|       0600Z --> Enter 2       |"
    echo "|       1200Z --> Enter 3       |"
    echo "|       1300Z --> Enter 4       |"
    echo "|       1630Z --> Enter 5       |"
    echo "|       2000Z --> Enter 6       |"
    echo "|===============================|"
    read -p "Enter time option (1-6): " TIME

    while [[ ! $TIME =~ [1-6] ]]; do
  	   read -p "Not a valid option. Enter time option (1-6): " TIME
    done

  else
    if [ $OUTLOOK == 2 ]; then
      echo "|===============================|"
      echo "|  Choose Outlook Time (DAY 2)  |"
      echo "|===============================|"
      echo "|       0700Z --> Enter 1       |"
      echo "|       1630Z --> Enter 2       |"
      echo "|===============================|"
      read -p "Enter time (1-2): " TIME

      while [[ ! $TIME =~ [1-2] ]]; do
  	   read -p "Not a valid option. Enter time option (1-2): " TIME
      done
    fi
  fi
}

read -p "Enter date (MM/DD/YYYY): " date
while [[ "$condition" = false ]]; do
	checkDate
done

echo "|=========================|"
echo "|    Choose Day Outlook   |"
echo "|=========================|"
echo "|    Day 1 --> Enter 1    |"
echo "|    Day 2 --> Enter 2    |"
echo "|    Day 3 --> Enter 3    |"
echo "|    Day 4 --> Enter 4    |"
echo "|=========================|"
read -p "Enter outlook (1-4): " OUTLOOK
while [[ ! $OUTLOOK =~ [1-4] ]]; do
  checkForecast
done

if [[ $OUTLOOK = 4 ]]; then
	OUTLOOK=48
fi

checkTime

echo "Retrieving the day $OUTLOOK outlook from $MONTH/$DAY/$YEAR."

url=`python lookup_coords.py $OUTLOOK $YEAR $MONTH $DAY $TIME`
python plot_categorical.py $OUTLOOK $url
