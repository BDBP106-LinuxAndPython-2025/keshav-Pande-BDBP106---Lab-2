# a=[]
# for i in range(1,51):
#     a.append(i)
# print(a)

#Q1.1
a=[]      #Create a empty list
b=[ i for i in range(1,51)]  # we define i in range (1,51) to print from 1 to 51
print(b)

# Q1.2 Slicing with positive step:
c=b[1:5]
print(c)

d=b[3:20:2]
print(d)

e=b[::2]
print(e)

f=b[10::2]
print(f)

g=b[1:1:1]
print(g)

h=b[:0:]
print(h)

i=b[-7::1]
print(i)

j=b[-6:]
print(j)

k=b[-10:-4]
print(k)

#iii)   Slicing with Negative step :
l=b[::-1]
print(l)

m=b[::-3]
print(m)

n=b[:1:-2]
print(n)

o=b[-1:-1:-1]
print(o)

p=b[-5:-1]
print(p)

q=b[:0:-1]
print(q)

r=b[:-1:1]
print(r)

s=b[-1:5:-1]
print(s)

t=b[2:2:-1]
print(t)
u=b[2:1:-1]
print(u)

v=b[0:-5]
print(v)

w=b[1:51:2]
print("the even list:-",w)

# 1.4
first_ten=b[:10]
print(first_ten)
even_35_50 =[i for i in b[35::] if i%2==0]
print(even_35_50)

new_list=first_ten+even_35_50
print(new_list)
