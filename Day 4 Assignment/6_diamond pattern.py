n=int(input("Enter no. of rows: "))
#top half
for r in range(1,n):
    #for spaces
    for s in range(n,r,-1):
        print(" ",end="")
        #for stars
    for st in range(1,2*r):
        print("*",end="")
    print("")
#second Half
for r in range(n,0,-1):
    #for spaces
    for s in range(n,r,-1):
        print(" ",end="")
    for st in range(1,2*r):
        print(" ",end="")
    print("")
        
    






  
#k = 2 * n - 2
#for i in range(0, n):
 #   for j in range(0, k):
  #      print(end=" ")
   # k = k - 1
    #for j in range(0, i + 1):
     #   print("* ", end="")
    #print("")
    
#k = rows - 2

#for i in range(rows, -1, -1):
 #   for j in range(k, 0, -1):
  #      print(end=" ")
   # k = k + 1
    #for j in range(0, i + 1):
     #   print("* ", end="")
   # print("")
