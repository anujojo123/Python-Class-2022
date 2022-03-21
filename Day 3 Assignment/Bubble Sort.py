data=[45,67,95,26,56,23,68,10,56]
size=len(data)
for i in range(size-1,0,-1):
    for j in range(0,i):
        if(data[j]>data[j+1]):
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp
print(data)
