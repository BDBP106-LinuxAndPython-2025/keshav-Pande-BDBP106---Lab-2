#!/bin/bash 

#For sorting each column

#For first column
sort -k 1 pig_weights.txt > column1.csv

#to check if save file is sorted 
cat column1.csv


#For Second column
sort -k 2 pig_weights.txt > column2.csv

#to check if save file is sorted
cat column2.csv


#For third column
sort -k 3 pig_weights.txt > column3.csv

#to check if save file is sorted
cat column3.csv


#For first column
sort -k 4 pig_weights.txt > column4.csv

#to check if save file is sorted
cat column4.csv



