# Write a script to find the first occurrence of a character, c, in a string S.
s=str(input("Enter the binary string: "))
c=str(input("Enter the character string: "))
count=0
for i in range(len(s)):
    if s[i]==c:
        count=count+2
        print(i+1)
        break
