'''a=7
b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))'''

class mahabub:
    def __init__(self,no):
        self.no=no
    def __add__(self, other):
        return self.no+other.no

    def show(self):
        print(self.no)
number1=mahabub(10)
number2=mahabub(20)
#print(number1.no)
#print(number1.__add__(number2))
print(number1+Number2)