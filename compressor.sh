#!/bin/bash

FOLDER=$1;
STRIPPED_PATH=`dirname $1`
COMPRESSED="compressed_"`basename $FOLDER`
echo "$STRIPPED_PATH/$COMPRESSED"
if [ ! -d "$STRIPPED_PATH/$COMPRESSED" ]; then
	mkdir "$STRIPPED_PATH/$COMPRESSED"
	echo "$STRIPPED_PATH/$COMPRESSED created"
fi
cd $FOLDER
for PHOTO in *.{jpg,JPG,jpeg,JPEG}
do
	if [ -f "$FOLDER/$PHOTO" ]; then
		BASE=$(basename "$PHOTO")
		FILENAME=${BASE%.*}
		EXTENSION=${BASE##*.}
		echo $FILENAME$EXTENSION
		convert "$FOLDER/$PHOTO" -sampling-factor 4:2:0 -strip -quality 85 -interlace JPEG -colorspace RGB "$STRIPPED_PATH/$COMPRESSED/$BASE"
	fi
done

for PHOTO in *.{png,gif,PNG,GIF}
do
	if [ -f "$FOLDER/$PHOTO" ]; then
		BASE=$(basename "$PHOTO")
		echo $PHOTO;
		convert "$FOLDER/$PHOTO" -strip -alpha Remove "$STRIPPED_PATH/$COMPRESSED/$BASE"
	fi
done
