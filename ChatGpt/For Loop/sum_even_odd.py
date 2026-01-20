# Find the sum of even numbers from 1 to N.
num=int(input("Enter The a Nth Number to print all Even and Odd is:-"))
e_sum=0
o_sum=0
for i in range(1,(num+1)):
    if i%2==0:
        e_sum+=i
    else:
        o_sum+=i
print("Sum of all Even Numbers is:-",e_sum)
print("Sum of all Odd Numbers is:-",o_sum)