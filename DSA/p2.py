"""
*
**
***
****
*****
"""
r=int(input("Enter a Number of Row:-"))
for i in range(1,r+1):
    for j in range(1,i):
        print("*",end=" ")
    print()