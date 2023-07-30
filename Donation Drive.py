# #A blood drive aims to collect 
# �
# N number of blood donations.
# The drive has collected 
# �
# X donations so far. Find the remaining number of donations needed to reach the target.


#Solution that worked for me:

z=int(input(""))

for i in range (0,z):
    x=input("")
    y= x.split()
    a= int(y[0])
    b= int(y[1])
    print(a-b)