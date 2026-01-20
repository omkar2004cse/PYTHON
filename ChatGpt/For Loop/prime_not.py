# Check whether a number is prime or not.
n=int(input("Input a Number:-"))
flag=False
if n<2:
    print("Number is Less than 2 is Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
        else:
            continue
if flag==True:
    print("is Not Prime Number:-")
else:
    print("is Prime Number")