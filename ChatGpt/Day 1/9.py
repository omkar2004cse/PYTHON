# Print the multiplication table of a given number up to 10.

num=int(input("Enter a Number to print table:-"))
print("Multiplication table of ",num)
for i in range(1,11):
    print(num*i)