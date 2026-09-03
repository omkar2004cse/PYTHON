# Find the largest of three numbers.

num1=int(input('Enter a Frist Number:-'))
num2=int(input('Enter a Second Number:-'))
num3=int(input("Enter a Third Number:-"))

# find greatest from three number

# if num1>num2:
#     if num1>num3:
#         print(num1,"is Greater than",num2,num3)
#     else:
#         print(num3,"is Greater than",num1,num2)
# else:
#     if num2>num3:
#         print(num2,"is Greater than",num1,num3)
#     else:
#         print(num3,'is Greater than',num1,num2)


# find smallest number from among three number

if num1<num2:
    if num1<num3:
        print(num1,"is Less than",num2,num3)
    else:
        print(num3,"is Small than",num1,num2)
else:
    if num2<num3:
        print(num2,"is Small than",num1,num3)
    else:
        print(num3,'is Small than',num1,num2)