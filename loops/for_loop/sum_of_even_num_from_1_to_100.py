print("Even number between 1 to 100 is:-")
sum=0
for i in range(1,101):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum of all even number 1 to 100 is:-",sum)