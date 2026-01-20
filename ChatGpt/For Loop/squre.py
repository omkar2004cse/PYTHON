# Print the square of numbers from 1 to 10.
l=[]
print("Square of 1 to 10 Numbers:-")
for i in range(1,11):
    print(i,"-",i**2)
    l.append(i**2)
print("Squres in List is:-",l)