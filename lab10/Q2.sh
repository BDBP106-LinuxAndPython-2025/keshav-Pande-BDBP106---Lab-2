# Q.2)Write a shell script that prompts the user to enter their age, and then checks if the age is greater than or equal to 18. If it is, print ”You are an adult”, otherwise print ”You are a minor.” (Note: the logical condition to test here will use -ge)

#!/bin/bash
#method1

echo "Enter the number :"
read n
echo "Your Number is $n"
if [ "$n" -gt 18 ]; then 
	echo "You are adult"
else 
	echo "You are minor "
fi
