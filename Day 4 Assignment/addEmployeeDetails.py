
eid=input("enter employee id : ")
name=input("Enter employee name :")
salary=input("enter your salary :")

#write to file, a stands for append
f1=open("mydata.txt","a")
f1.write(eid+","+salary+"/n")
f1.close()

print("Employee data saved successfully")
