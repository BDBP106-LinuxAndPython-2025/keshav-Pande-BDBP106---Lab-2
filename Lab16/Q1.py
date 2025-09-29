# Write a script to convert the binary number B into decimal
num=str(input("Enter a number: "))
r=str(num[::-1])
power=0
sum=0
for i in r:
    if int(i)==0 or int(i)==1:
      sum=sum+(int(i)*2**power)
      power=power+1
    else:
        sum=0
        print(f'The number is not binary ')
        break
print(f'Sum: {sum}')