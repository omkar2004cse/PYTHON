# Reverse a given integer.

number=int(input("Enter Number:-"))
temp=number
rev=0
print
while temp>0:
    n=temp%10
    rev=rev*10+n
    temp=temp//10

print(rev)
print(type(rev))

