# Chef has been working hard to compete in MasterChef.
# He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.Check whether
# Chef made it to the top 10 or not

#Solution that worked for me:

# cook your dish here
z=int(input(""))

for i in range (0,z):
    x=int(input(""))
    if x<=10:
        print("YES")
    else:
        print("NO")
    i=i+1