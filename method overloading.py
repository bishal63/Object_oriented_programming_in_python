'''class name:
    def mahabub(self,num1,num2,num3):
        print(num1*num2*num3)
name1=name()
name1.mahabub(20,3,4)'''

'''class mahabub:
    def alam(self,num1,num2=None,num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1*num2*num3)
        elif num1 != None and num2 != None:
            print(num1*num2)
        else:
            print(1*num1)
bishal=mahabub()
bishal.alam(2,3,5)

class mahabub:
    def alam(self,num1,num2=None,num3=None):
        if num1 != None and num2 != None  and num3 != None:
            print(num1+num2+num3)
        elif num1 != None and num2 != None:
            print(num1+num2)
        else:
            print(num1)
bishal=mahabub()
bishal.alam(3,4,5)'''


'''class mahabub:
    def alam(self, *nums):
        bishal = 1
        for x in nums:
            bishal = bishal * x
            print(bishal)


mahim = mahabub()
mahim.alam(2)
mahim.alam(2, 5)'''

#metod overloading in multiple dispatch

'''from multipledispatch import dispatch
class mahabub:
    dispatch(int,int)
    def bishal(self,a,b):
        print(a*b)

alam=mahabub()
alam=bishal(5,4)'''

'''from multipledispatch import dispatch
class mahabub:
    dispatch(str,str)
    def alam(self,a,b):
        print(str(a)*str(b))
bishal=mahabub()
bishal=alam(3,4)'''



