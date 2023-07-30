# The working hours of Chef’s kitchen are from 
# �
# X pm to 
# �
# Y pm 
# (
# 1
# ≤
# �
# <
# �
# ≤
# 12
# )
# (1≤X<Y≤12).

# Find the number of hours Chef works.


#Solution the worked for me:
# cook your dish here
z=int(input(""))

for i in range (0,z):
    x=input("")
    y= x.split()
    a= int(y[0])
    b= int(y[1])
    print(b-a)