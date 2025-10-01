# Write a script to replace all occurrences of a character, c, with another character, d.
s= str(input("Enter the string:"))
c=input("Enter the character you want to replace")
d=input("Enter the character you want to add")
s_mod=""
if i in range(len(s)):
    if s[i]==c:
        s_mod=s_mod+d
    else:
        s_mod=s_mod+s[i]
print(s_mod)

