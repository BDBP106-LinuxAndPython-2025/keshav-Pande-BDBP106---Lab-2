#!/bin/bash

#for sorting the data in Height column from the data-file 'SOCR-HeightWeight.csv'

sort -t "," -k2 -nr SOCR-HeightWeight.csv -o Height.csv

#for checking if the file has been sorted or not 

cat Height.csv

