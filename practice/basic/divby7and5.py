# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
print("number is divisible by 7 and multiple of 5 between 1500 and 2700 is:-")
for x in range(1500,2700):
    if(x%7==0):
        if(x%5==0):
            print(x)