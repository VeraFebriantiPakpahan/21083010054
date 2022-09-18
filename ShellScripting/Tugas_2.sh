#!/bin/bash

a=10
b=0

if [ $a -gt $b ]
then
  echo "angka merupakan bilangan positif"
elif [ $a -lt $b ]
then
  echo "angka merupakan bilangan negatif"
else
  echo "angka merupakan nol"
fi
