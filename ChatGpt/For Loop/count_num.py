# Count how many numbers between 1 and 100 are divisible by 3
num=int(input("Enter a Nth Number:-"))
count=0
for i in range (1,(num+1)):
    if i%3==0:
        count+=1
        print(i,end=" ")
print("Count of Numbers is Divisible by are:-",count)