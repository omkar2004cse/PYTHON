# rint all even and odd numbers between 1 and n.
n=int(input("Enter a Nth Number:-"))
even=[]
odd=[]
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even:-",even)
print("odd:-",odd)