#!/bin/bash

#create the file using touch command 
touch file1 file2a

#check file permission using 
ls -l 

#change permission using chmod for user to execute 
chmod u+x file1 
chmod u+x file2a 

#check file permission granted using 
ls -l 
