# Find the factorial of a number.

num=int(input("Enter a Number:-"))
fact=1
temp=num
while temp>0:
    fact=fact*temp
    temp=temp-1

print('Factorial of',num,"is:-",fact)