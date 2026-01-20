# Print all odd numbers between 1 and 50.
n=int(input("Enter a Nth number to print ODD number:-"))
for i in range(1,(n+1)):
    if i%2!=0:
        print(i,end=" ")