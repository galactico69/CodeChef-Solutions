# Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is 
# �
# X. Our Chef has already ‘Attempted’ 
# �
# Y problems among them. How many problems are yet ‘Un-attempted’?

#Solution that worked for me

x=input("")
y= x.split()
a= int(y[0])
b= int(y[1])
print(a-b)