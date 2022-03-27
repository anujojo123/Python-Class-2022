class Algebra:
    def add(a,b):
        return a+b
    def mul(a,b):
        return a*b
class Trignometry:
    def sin0():
        return 0
    def cos0():
        return 1
class TotalMaths(Algebra,Trignometry):
    def sub(a,b):
        return a-b
    def sub(a,b):
        return a-b

print(TotalMaths.sub(5,2))
print(TotalMaths.mul(5,2))
