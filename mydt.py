#TUPLES
#program to create a tuple with different data types and do various operations

#1.find length of tuple

tup1=('maruti','wagonr','5','1.1','10')
print("the length of the tuple is:",len(tup1))
print("\n")

#2.find largest and smallest elements of a tuple

tup2=('ram','shyam','heena','rekha')
print("min in tuple 2:",min(tup2))
print("max in tuple 2:",max(tup2))
tup3=('23','10','2','0.2','11.1')
print("min in tuple 3:",min(tup3))
print("max in tuple 3:",max(tup3))
tup4=('ram','5','aman','12','0.1')
print("min in tuple 4:",min(tup4))
print("max in tuple 4:",max(tup4))
print("\n")

#3.find product of all elements of a tuple

tup5=(1,2,3,4,5)
res=1
for i in tup5 :
    res=res*i

print("product of all elements of tuple are :", res)
print("\n")

#SETS
#1.create two sets using user defined values

s1=input("enter first value")
s2=input("enter second value")
s3=input("enter third value")
my_set={s1,s2,s3}

print(my_set)
r1=input("enter first value")
r2=input("enter second value")
r3=input("enter third value")
my_rset={r1,r2,r3}
print(my_rset)
print("\n")

#1.1.difference between two sets
A={1,2,3,4,5,6}
B={4,5,6,7,8,9}
print("the set difference is :",B-A)
print("\n")

#1.2.compare two sets
set_a={'blue','green','red','yellow'}
set_b={'blue','green'}
x=set_a<=set_b
print(x)
y=set_a>=set_b
print(y)
print("\n")

#1.3.print the result of intersection of two sets
set_x={'blue','grey','white','red'}
set_y={'grey','white','yellow','scarlet'}
print("intersection of sets is:" ,set_x&set_y)
print("\n")

#DICTIONARIES
#create a dictionary to store name and marks of 10 students by user input

d1=input("enter the name of student")
v1=input("enter the marks of student")
d2=input("enter the name of student")
v2=input("enter the marks of student")
d3=input("enter the name of student")
v3=input("enter the marks of student")
d4=input("enter the name of student")
v4=input("enter the marks of student")
d5=input("enter the name of student")
v5=input("enter the marks of student")
d6=input("enter the name of student")
v6=input("enter the marks of student")
d7=input("enter the name of student")
v7=input("enter the marks of student")
d8=input("enter the name of student")
v8=input("enter the marks of student")
d9=input("enter the name of student")
v9=input("enter the marks of student")
d10=input("enter the name of student")
v10=input("enter the marks of student")
my_dict={d1:v1,d2:v2,d3:v3,d4:v4,d5:v5,d6:v6,d7:v7,d8:v8,d9:v9,d10:v10}
print(my_dict)
print("\n")


