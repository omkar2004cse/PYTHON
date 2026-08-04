# Swap two numbers without using a third variable.

n1=int(input("Enter a Frist Number:-"))
n2=int(input("Enter a Second Number:-"))
print("Before Swapping a=",n1,"\t b=" ,n2)
# n1=n1+n2
# n2=n1-n2
# n1=n1-n2
# print("After Swapping a=",n1,"\t b=",n2)

# Swap two numbers using a third variable.

n3=n1
n1=n2
n2=n3
print("After Swapping a=",n1,"\t b=",n2)