# Swap two numbers (with and without using a third variable).

n1=int(input("Enter a Frist Number:-"))
n2=int(input("Enter a Second Number:-"))
print("before Swaping:-")
print(f'n1: {n1}        n2: {n2}')

print("After Swaping:-")
n1=n1+n2
n2=n1-n2
n1=n1-n2

print(f'n1: {n1}        n2: {n2}')


# using third varible 

num1=int(input("Enter a Number_1:-"))
num2=int(input("Enter a Number_2:-"))
c=None
print(f'Before Swaping\nn1:{num1}   n2:{num2}')

c=num2
num2=num1
num1=c
print(f'After Swaping\nn1:{num1}    n2: {num2}')