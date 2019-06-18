# -*- coding: utf-8 -*-

class calc():
    def add(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.res=n1+n2
        return res
    
    def sub(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.res=n1-n2
        return res
    
    def div(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.res=n1/n2
        return res
    
    def mul(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.res=n1*n2
        return res
    
    def info(self):
        print('n1',self.n1,'n2',self.n2,'Result:',self.res)
        
a= calc()
res=a.add('17','10')
res=a.info()

b=calc()
res=b.sub('20','10')
res=b.info()

c= calc()
res=c.div('15','3')
res=c.info()

d= calc()
res=d.mul('5','5')
res=d.info()







class calc():
    def add(self,n1,n2):
        return(n1+n2)
    def sub(self,n1,n2):
        return(n1-n2)
    def mul(self,n1,n2):
        return(n1*n2)
    def div(self,n1,n2):
        return(n1/n2)
cal=calc() 
res=cal.add(10,20)  
print('result of addition',res)
print(cal.sub(20,10))
print(cal.mul(5,5))
print(cal.div(15,3))









