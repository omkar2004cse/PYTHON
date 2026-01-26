# Print all prime numbers between 1 and 100.
n=int(input("Enter a Nth element is:-"))
flage=False
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            flage=True
            break
        else:
            flage=False
            continue
    if flage==False:
        print(i,end=" ")