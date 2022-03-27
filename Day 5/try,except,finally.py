try:
    x=input("Enter first number: ")
    y=input("Enter second number: ")
    z=x/y
    print(y)
    input()
except ValueError:
    print("only Numbers can be Entered")

except ZeroDivisionError:
    print("cannot divided by Zero")
except:
    print("some other error, Contact admin")
finally:
    print("by Anu Wilson")
input()
