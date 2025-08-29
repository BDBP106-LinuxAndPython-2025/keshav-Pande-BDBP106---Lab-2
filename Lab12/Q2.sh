 #!/bin/bash 

#print even numbers between 0 and 50 using for-loop

for (( i=0 ; i<=50; i=i+2))
do 
	echo $i
done

#print even numbers between 0 and 50 using while loop
n=0
while [ $n -le 50 ]
do 
	x=$[ n%2 ]
if [ $x -eq 0 ]; then
	echo "the even number are:"$n
fi 
n=$[ $n+1 ]
done


#print even numbers between 0 and 50 using untill 
 
 n=0
 until [ $n -lt 51 ]
 do
            echo $n
                n=$[$n+2]
        done


