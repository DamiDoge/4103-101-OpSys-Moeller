#!/bin/bash

filename=/usr/share/dict/words
#get a random number outside of the range of $RANDOM
rand="$(shuf -i 1-99171 -n 1)"

counter=0
while read -r line
do
	let counter=counter+1
    name="$line"
	if [[ $counter -eq $rand ]]
	then
		echo $line
		break
	fi
#end the loop and tell read what file to look at.
done < "$filename"