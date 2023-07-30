# Chef appeared for a placement test.

# There is a problem worth 
# �
# X points. Chef finds out that the problem has exactly 
# 10
# 10 test cases. It is known that each test case is worth the same number of points.

# Chef passes 
# �
# N test cases among them. Determine the score Chef will get.

# NOTE: See sample explanation for more clarity.



#Solution that worked for me:

z=int(input(""))

for i in range (0,z):
    x=input("")
    y= x.split()
    a= int(y[0])
    b= int(y[1])
    c=a/10
    q=int(c)
    print(q*b)
    i=i+1