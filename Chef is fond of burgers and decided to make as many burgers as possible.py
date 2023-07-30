# Chef is fond of burgers and decided to make as many burgers as possible.
# Chef has A patties and B buns. To make 11 burger, Chef needs 11 patty and 11 bun.
# Find the maximum number of burgers that Chef can make.


#Solution that worked for me:

z=int(input(""))

for i in range (0,z):
    x=input("")
    y= x.split()
    a= int(y[0])
    b= int(y[1])
    if a<b:
        print(a)
    else:
        print(b)
        
    i=i+1
