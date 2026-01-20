# Print all even numbers between 1 and 50.
n=int(input("Give Input to Print the all Even Number Between them:-"))
print("Even Number are:-")
for i in range(1,(n+1)):
    if i%2==0:
        print(i,end=" ")