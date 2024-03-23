##def is_prime():
##    n=int(input('enter the number'))
##    f=1
##    
##    for i in range(2,n):
##        if n%i==0:
##            f=0
##            break
##    if f==0:
##        print(' not prime')   
##                   
##    else:
##        print(' prime')
##        
##is_prime()


##def avg(a,b,c):
##    op=(a+b+c)/3
##    print(op)
##avg(3,2,1)
            
    

##def login():
##    n=1
##    while n!=0:
##    
##        user_name=input('user name :')
##        password=input('password :')
##        if password==user_name:
##            print('wellcome')
##            n=0
##        else:
##            print('wrong password')
##        
##login()


##def fib(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fib(n-1)+fib(n-2)
##a=fib(5)
##print(a)



def power(n,m):
    if m==0:
        return 1
    
    return n*power(n,m-1)

a=power(2,3)
print(a)






