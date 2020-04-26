#! /bin/bash
echo "we need to extract depth maps"

listOfPhotos=$( ls ./targetPhotos )
echo $listOfPhotos

for i in $listOfPhotos
do
	currentName=$i
	lengthOfString=${#currentName}
	(( lengthOfString-= 4)) # here the length of string means the first part of the name without .jpg
	depthName=${currentName:0:lengthOfString}d #we extracted the substring with just the name and appended the d to indicate depth
	depthName=$depthName.tiff
	./exiftool -b -depthMapTiff ./targetPhotos/$currentName > ./targetPhotos/$depthName
done
echo depth maps have been generated
