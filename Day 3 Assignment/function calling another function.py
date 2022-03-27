def factorial(n):
    fact=1

    for i in range(1,n+1)
        fact=fact*i
    return fact

def nPr(n,r):
    perm= factorial(n)//factorial(n-r)
    return perm

def nCr(n,r):
    comb=factorial(n)//factorial(n-r)*factorial(r)
    return comb

n=int(input("Enter a value :"))
fct= factorial(n)
print("The factorial of the number is :",fct)


npr=nPr(n,)

