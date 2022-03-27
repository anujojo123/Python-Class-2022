class Employee:
    #constructor
    #def __init__(self,id,name,salary):
        #self.id=id
        #self.name=name
        #self.salary=salary
    
    #Methods
    def readData(self):
        self.id=int(input("Enter employee id: "))
        self.name=input("Enter employee name: ")
        self.salary=int(input("Employee salary "))
    def printData(self):
        print("ID= ",self.id)
        print("Name= ",self.name)
        print("salary= ",self.salary)
        print("Company","Microsoft")

        
#e1=Employee(0," ",0)       for constructor
e1=Employee()
e1.readData()
e1.printData()
