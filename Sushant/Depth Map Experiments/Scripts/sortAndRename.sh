#! /bin/bash

#This script renames the files which are sorted according to z. The value of z-barred (zb) goes from 15 to 135 (except 70)



stepSize=5 #this is so because we are increasing value of zb by 5cm
listOfFiles=$( ls )
cameraToWall=150 #this is the distance of the camera to the wall
zb=15 #this is the initial value of zb

nameOfCallingScript=$0 #this still has a "./" before its name
nameOfCallingScript=${nameOfCallingScript:2} #this removes the ./ before its name


for i in $listOfFiles
do
	if [ $nameOfCallingScript = $i ] # we are just skipping over the part where the list of the file contains the name of script
	then
	continue
fi

z=$(( $cameraToWall - $zb  ))
echo $z $zb
mv $i $z.jpg


((zb+=stepSize))

if [ $zb -eq 70 ]
then
	((zb+=stepSize))
fi

done


