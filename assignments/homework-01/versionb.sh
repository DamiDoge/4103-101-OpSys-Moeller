#!/bin/bash

#removes the directory path from the file
filename=$(basename "$1")
#grabs everything after the period to hold the file extension
extension="${filename##*.}"
#then grab everything before the period to perserve the filename
filename="${filename%.*}"
verdate=`date +%Y-%m-%d`
#put it all together and
verfile=$filename'_'$verdate'.'$extension
#now you got a file
cp $1 $verfile