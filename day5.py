##def check(n):
##    if n%10==5:
##        return n**2
##    elif n%10==3:
##        return n**3
##    elif n%10==6:
##        return n-1
##    else:
##        return n/2
##
##a=check(32)
##print(a)


##class
##class f15:
##    def light(self):
##        print('lights are on')
##    def fan(self,speed):
##        print('fan is on and the speed is',speed)
##        self.s=speed
##    def cpu(self):
##        print('powering on the system')
##        print(self.s)
##jaggu=f15()
##jaggu.light()
##jaggu.fan(5)
##jaggu.cpu()


##class shopping:
##    def __init__(self,place):
##        self.place=place
##        print('enjoy at',place)
##    def dress_type(self,dt):
##        #print('which type of dress you need:',dt)
##        self.t=dt
##    def price(self,pr):
##        #print('max price of the dress',pr)
##        self.p=pr
##    def dresssize(self,sz):
##        #print('required size',sz)
##        self.s=sz
##    def display(self):
##        print('which type of dress you need:',self.t)
##        print('max price of the dress:',self.p)
##        print('required size:',self.s)
##        print('thankyou for visiting ',self.place ,'visit again')
##total=shopping('KLM')
##total.dress_type('shirts')
##total.price(3000)
##total.dresssize('l')
##total.display()

#inheritance
#highrarichi
##class a:
##    def hi(slef):
##        print("hi")
##    def h(self):
##        print('how')
##class b(a):
##    def hii(self):
##        print("r")
##obj2=b()
##
##class c(a):
##    def he(self):
##        print('u')
##obj3=c()
##obj3.hi()
##obj2.h()
##obj2.hii()
##obj3.he()


#multi level inheritance
##class a:
##    def hi(slef):
##        print("hi")
##    def h(self):
##        print('how')
##class b(a):
##    def hii(self):
##        print("r")
##class c(b):
##    def he(self):
##        print('u')
##obj3=c()
##obj3.hi()
##obj3.h()
##obj3.hii()
##obj3.he()

####multiple inheritance
####class a:
####    def hi(slef):
####        print("hi")
####    def h(self):
####        print('how')
####class b(a):
####    def hii(self):
####        print("r")
####
####class c(a,b):
####    def he(self):
####        print('u')
####obj3=c()
####obj3.hi()
####obj3.h()
####obj3.hii()
####obj3.he()      
####

#multi level inheritance
##class a:
##    def hi(slef):
##        print("hi")
##    def hi(self,h):
##        print('how',h)
##obj=a()
##obj.hi(5)
##        


'''class carshowroom:
    def __init__(self):
        cgst=2000
        sgst=1000
        insurence=45000
        amount=cgst+sgst+insurence
        self.amount=amount
    def company(self,company_name):
        company_name=input('enter the name')
        print('wellcome to ',company_name,'family')
        self.company_name=company_name
        
    def model(self,model):
        if self.company_name=='mahendra':
            l1=['thar','xuv700']
            print(l1)
        elif self.company_name=='volkswagen':
            l2=['virtus','taigun']
            print(l2)
        elif self.company_name=='toyota':
            l3=['vellfire','fortuner']
            print(l3)
        else:
            print('not found')
        

        modelname=input('enter the model')
        self.model=model
        print(self.model)
    def price(self):
        if self.model=='thar':
            exshowroom=1410000
            print('x-showroom price:1410000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='xuv700':
            exshowroom=2699000
            print('x-showroom price:2699000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='virtus':
            exshowroom=1941000
            print('x-showroom price:1941000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='taigun':
            exshowroom=1170000
            print('x-showroom price:1170000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='vellfire':
            exshowroom=13000000
            print('x-showroom price:13000000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='fortuner':
            exshowroom=5144000
            print('x-showroom price:5144000')
            print('onroad price:',exshowroom+self.amount)
        else:
            print('not found')
obj=carshowroom()
obj.company('company_name')
obj.model('model')
obj.price()'''

class carshowroom:
    def _init_(self):
        cgst=2000
        sgst=1000
        insurence=45000
        amount=cgst+sgst+insurence
        self.amount=amount
    def company(self,company_name):
        company_name=input('enter the name')
        print('wellcome to ',company_name,'family')
        self.company_name=company_name
        
    def model(self,model):
        if self.company_name=='mahendra':
            l1=['thar','xuv700']
            print(l1)
        elif self.company_name=='volkswagen':
            l2=['virtus','taigun']
            print(l2)
        elif self.company_name=='toyota':
            l3=['vellfire','fortuner']
            print(l3)
        else:
            print('not found')
        return model()

        modelname=input('enter the model')
        self.model=model
        print(self.model)
    def price(self):
        if self.model=='thar':
            exshowroom=1410000
            print('x-showroom price:1410000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='xuv700':
            exshowroom=2699000
            print('x-showroom price:2699000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='virtus':
            exshowroom=1941000
            print('x-showroom price:1941000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='taigun':
            exshowroom=1170000
            print('x-showroom price:1170000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='vellfire':
            exshowroom=13000000
            print('x-showroom price:13000000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='fortuner':
            exshowroom=5144000
            print('x-showroom price:5144000')
            print('onroad price:',exshowroom+self.amount)
        else:
            print('not found')
obj=carshowroom()
obj.company('company_name')
class carshowroom:
    def _init_(self):
        cgst=2000
        sgst=1000
        insurence=45000
        amount=cgst+sgst+insurence
        self.amount=amount
    def company(self,company_name):
        company_name=input('enter the name')
        print('wellcome to ',company_name,'family')
        self.company_name=company_name
        
    def model(self,model):
        if self.company_name=='mahendra':
            l1=['thar','xuv700']
            print(l1)
        elif self.company_name=='volkswagen':
            l2=['virtus','taigun']
            print(l2)
        elif self.company_name=='toyota':
            l3=['vellfire','fortuner']
            print(l3)
        else:
            print('not found')
            a=company()
            return a
        

        modelname=input('enter the model')
        self.model=model
        print(self.model)
    def price(self):
        if self.model=='thar':
            exshowroom=1410000
            print('x-showroom price:1410000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='xuv700':
            exshowroom=2699000
            print('x-showroom price:2699000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='virtus':
            exshowroom=1941000
            print('x-showroom price:1941000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='taigun':
            exshowroom=1170000
            print('x-showroom price:1170000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='vellfire':
            exshowroom=13000000
            print('x-showroom price:13000000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='fortuner':
            exshowroom=5144000
            print('x-showroom price:5144000')
            print('onroad price:',exshowroom+self.amount)
        else:
            print('not found')
obj=carshowroom()
obj.company('company_name')
obj.model('model')

obj.price()
                
