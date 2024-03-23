##n=12467
##while n>0:
##    a=n%10
##    print(a)     printing the digits
##    n=n//10

##n=12345
##s=0
##while n>0:
##    a=n%10
##    s=s+a        sum of digits
##    n=n//10
##print(s)

####n=43536
####s=0
####while n>0:
####    a=n%10         #no of digits
####    s=s+1
####    n=n//10
####print(s)    

##n=12467
##s=0
##while n>0:
##    a=n%10
##    if a%2==0:
##        s=s+1
##                  #no of even digits
##    n=n//10
##print(s)   

##n=12
##i=0
##a=1
##while a<n:
##   if n%a==0:       sum of factors
##       print(a)
##       i=i+a
##   a=a+1
##print(i)  


##n=47
##i=0
##c=n
##while n>0:
##    a=n%10
##    i=i+a         div by its sum of digits
##    n=n//10
##print(i)
##if c%i==0:
##    print('div')
##else:
##    print('not div')




#sum of di gits whose digit is powered by its total digno

##n=153
##i=0
##s=0
##c=n
##d=c
##while n>0:
##    
##    s=s+1
##    n=n//10
##while c>0:       arm strong number 
##    a=c%10
##    a=a**s
##    i=i+a
##    c=c//10
##print(i)
##if i==d:
##    print('yes')
##else:
##    print('no')
##
##


##n=1441                paladrom
##n1=n
##rev=0
##while n>0:
##    a=n%10
##    rev=rev*10+a
##    n=n//10
##    
##print(rev)
##if n1==rev:
##    print('paldrome')
##else:
##    print('not paldrome')



#lists
##jaggu=['jagadeesh','venkat','sai','vinay',]
##jaggu.append('s')
##jaggu.insert(2,'hi')
##print(jaggu[0])
##print(jaggu[1])
##print(jaggu[2])
##print(jaggu[3:5])
##print(jaggu[4])
##print(jaggu[::-1])
##
##print()
##for i in range(0,3):
##    print(jaggu[i])
##print()
##for i in jaggu:
##    print(i)
##jaggu[2]=5
##print(jaggu)



#tuple
##jaggu=('jagadeesh','venkat','sai','vinay',)
##jaggu=jaggu+('hi',)
##
##print()
##
##print()
##for i in jaggu:
##    print(i)
##print()
##print(type(jaggu))
##print(jaggu)


##l=[42,36,28,96,4,-1,1]
##s=999
##b=0
##for i in range(0,len(l)):    #sum of greater and smaller value of list
##    if l[i]<s:
##        s=l[i]
##    elif l[i]>b:
##        b=l[i]
##a=s+b   
#print(a)



#dictinory
##di={'name':'jaggu',
##       'rollno':427,
##       12:21}
##di['rollno']=35427
##di[23]=32
##for i in di:
##    print(i)
##for x in di.values():
##    print(x)
##for a,b in di.items():
##    print(a,b)
##di.pop(12)
##print(di)


##l1=[[1,2],['a','b'],['a1','b1']]
##print(l1[0])
##print(l1[2][0])
##print(l1[1][1])



s1={1,2,3,4,7}
s1.add(0)

s1.update([5,6])
s1.remove(7)
s1.add(1)
print(s1)







