# Reverse a given number using a loop.
num=int(input("Enter a Number to Reverse:="))
n=num
reverse=0
for i in range(num):
    l=num%10
    reverse=reverse*10+l
    num=num//10
    if num==0:
        break
print("You Entered Number is:-",n)
print("Reverse Number is:-",reverse)