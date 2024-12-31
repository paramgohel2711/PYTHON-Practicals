n=int(input("Enter The Term:"))
i=1
n1=0
n2=1
print(n1,end=" ")
print(n2,end=" ")
while i<n-1:
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    i=i+1
