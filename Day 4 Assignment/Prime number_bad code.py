n=int(input("Enter the value : :"))
counter=0
for i in range(1,n+1):
    if(n%i==0):
        counter=counter+1
        if(counter==2):
            print("The number is Prime")
        else:
            print("The number is not prime")
print()
            
