
ch="y"
while(ch=="y"):

    eid=input("enter employee id : ")
    name=input("Enter employee name :")
    salary=input("enter your salary :")

    #write to file, a stands for append
    f1=open("employeeData.txt","a")
    print("/n")
    f1.write(eid+","+name+","+salary+"\n")
    f1.close()

    print("Employee data saved successfully")
    ch=input("Do you want to add another employee :y/n")
    
    
