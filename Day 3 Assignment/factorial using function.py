def factorial(n):
    fact=1
    
    for i in range(1,n+1):
        fact=fact*i
    return fact


num=5
ans= factorial(num)
print("The factorial of ",num,"is : ",ans)

num=8
ans=factorial(num)
print("The Factorial of ",num,"is : ",ans)

num=10
ans=factorial(num)
print("The factorial of ",num," is : ",ans)
