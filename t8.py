a=int(input('enter the sub1'))
b=int(input('enter the sub2'))
c=int(input('enter the sub3'))
total=a+b+c
if a>80 and b>80 and c>80:
    print('a+')
elif (a>60 and a<80) and(b>60 and b<80)and (c>60 and c<80):
    print('b+')
else:
    print('pass')
