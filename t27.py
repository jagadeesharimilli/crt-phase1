
#for i in range(1,5):
 #   for j in range(1,i+1):
  #      print(j,end="")
   # print()


   
##n=1
##for i in range(1,5):
##    for j in range(1,i+1):
##    
##        
##    
##        print(n,end="")
##        n=n+1
##    print()


for i in range(1,5):
    for j in  range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print('*',end="")
        else:
            print(' ',end="")
    print()
