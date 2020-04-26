#! /bin/bash
echo "we need to extract depth maps"

listOfPhotos=$( ls ./targetPhotos )
echo $listOfPhotos

for i in $listOfPhotos
do
	currentName=$i
	depthName=${i:0:3}
	depthName=$depthName.tiff
	./exiftool -b -depthMapTiff ./targetPhotos >./targetPhotos/$depthName
done
