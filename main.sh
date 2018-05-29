#!/bin/bash

currenttime=$(TZ=GMT date +%H%M)
echo $currenttime

TIME=(0105 0605 1205 1305 1635 2005)

if [[ $TIME =~ $currenttime ]]
then 
	python ./source/getjson.py
fi


