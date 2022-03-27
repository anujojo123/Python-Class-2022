row=int(input("Enter the number of rows : "))
n=2*row-2

for i in range(0,row):
    for j in range(0,n):
        print(end=" ")
    n=n-1
    for j in range(0,i+1):
        print("* ",end="")
    print()

n=row-2
    
for i in range(row,-1,-1):
    for j in range(n,0,-1):
        print(end=" ")
    n=n+1
    for j in range(0,i+1):
        print("* ",end="")
    print("")
    input()
    
