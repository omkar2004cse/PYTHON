# Print all numbers divisible by 5 between 1 and 100.
n=int(input("Enter a Nth number:-"))
print("All Number between",n,"is Divisible by 5 is:-")
for i in range(1,(n+1)):
    if i%5==0:
        print(i,end=" ")