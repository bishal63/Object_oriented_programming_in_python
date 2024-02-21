'''class number:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x + other.x

number1=number(20)
number2=number(30)
number3=number("mahabub")
number4=number("CSE")
print(number1+number2)
print(number3+number4)'''

'''class student:
    def __init__(self,y):
        self.y=y
    def __add__(self,other):
        return self.y+other.y




student1=student("mahabub")
student2=student("bishal")
print(student1+student2)'''

'''class house:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def view(self):
        print(self.x,self.y)

    def __add__(self,other):
        return self.x+other.x,self.y+other.y





h1=house(20,30)
h2=house(40,50)
h1.view()
h2.view()
print(h1+h2)'''


class house:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def view(self):
        print(self.x,self.y)

    def __add__(self,other):
        newx= self.x+other.x
        newy=self.y+other.y
        return "newx"+str( newx)+"newy"+str(newy)





h1=house(20,30)
h2=house(40,50)
h1.view()
h2.view()
print(h1+h2)