

ch="y"

#Read data from file
f1=open("employeeData.txt","r")
#read all the lines
allemployees=f1.readlines()
id=input("enter emp id:")

while(ch=="y"):
    isFound=False

    for emp in allemployees:
        data=emp.split(",")

        if data[0]==id:
            print("name = ",data[1])
            print("salary = ",data[2])
            isFound=True
            break
    if(isFound==False):
            
        #print("employee not found")
        ch=input("Do you want to search another employee(y/n):")
