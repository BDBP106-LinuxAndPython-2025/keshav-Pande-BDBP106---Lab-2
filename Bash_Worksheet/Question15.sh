#!/bin/bash
#(15) A script that finds files older than 7 days and compresses them into a .tar.gz file with the date of compression in the name in the format YYYYMMDD.
date=$(date +%Y%m%d)
find . -type f -mtime +7 | tar -cvf files_old$date.tar.gz
