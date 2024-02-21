#default class and object code
'''class mahabub:

    def __init__(self):
        print("tapo")
        print("vola")

bishal=mahabub()
alam=mahabub()
print(bishal,alam)'''

#value and attribute code(parameter)
"""class mahabub:
    def __init__(self,name,id):
        self.name=name
        self.id=id
bishal=mahabub("saikat",1)
alam=mahabub("mahim",2)
print(alam.id)
alam.id=10
print(alam.id)"""

#resume
'''class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
student1=student("mahabub",1)
student2=student("bishal",2)
print(student1.name)
student1.name="alam"
print(student1.name)

#instance variable ba object ar sokol item dekhar jonno
class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def details(self):
        print("name:", self.name, "id:", self.id)

student1=student("mahabub",100)
student2=student("alam",101)
student3=student("bishal",102)
student1.details()'''

'''class student:
    def __init__(self,name,dipartment,zila):
        self.name=name
        self.dipartment=dipartment
        self.zila=zila
    def details(self):
        print(self.name,self.dipartment,self.zila)

student1=student("mahabub","computer","dinajpur")
student1.details()'''

'''class dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def update_color(self,color):
        self.color=color
    def view(self):
        print(self.name,self.color,"is smailing")

dog1=dog("rover","black")
#dog1.view()
dog1.update_color("green")
#dog1.view()
#print(dog1.__dict__)
print(dir(dog1))'''

class student:
    def __init__(self,name,id,session):
        self.name=name
        self.id=id
        self.session=session
    def update_roll(self,roll):
        self.roll=roll

    def details(self):
        print(self.name,self.id,self.session)

student1=student("mahabub",121,2022)
student2=student("bishal",122,2023)
#student2.details()
student2.name="mahim"
#student2.details(
print(student2.__dict__)
print(dir(student2))

#set ar get method use kore value update kori
'''class book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.price=0
    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price
    def details(self):
        print("book name:",self.name,"author name:.",self.author,"price:",self.price)
book1=book("bonolota","jibonnanando")
book1.details()
book1.set_price(2220)
book1.details()'''

'''class car:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def set_owner(self,owner):
        self.owner=owner

    def get_owner(self):
        return self.owner
    def details(self):
        print("car name:",self.name,
              "\ncar model:",self.model,
              "\ncar price:",self.price,
              "\nowner:",self.owner)



car1=car("mercidies","aur2367",200000000)
car2=car("tata","auie975656",30000000)
#car2.details()
car2.set_owner("mahabub")
print(car2.get_owner())
car2.details()
print(car2.__dict__)
print(dir(car2))'''

#pass by refarence instance variable and method
'''class car:
    def __init__(self,room,door,window):
        self.room=room
        self.door=door
        self.window=window
    def details(self):
        print("room:",self.room,
              "\ndoor:",self.door,
              "\nwindow",self.window)
    def compare(self,room3):
        if self.window==room3.window:
            print("both are same",room3.window)
        else:
            print("not are same")
room1=car('4','6','12')
room2=car('6','8','12')
room2.details()
room1.details()
room1.compare(room2)'''

#pass by refrence exercise
'''class name:
    def __init__(self,profession,intress,zila):
        self.profession=profession
        self.intress=intress
        self.zila=zila

    def details(self):
        print(self.profession,self.intress,self.zila)

    def compare(self,mahim):
        if self.profession==mahim.profession:
            print("same",mahim.profession)
        else:
            print("not same")
mahabub=name("student","coding","dinajpur")
bishal=name("student","watching football","saidpur")
bishal.details()
bishal.compare(mahabub)'''

'''class name:
    def __init__(self,profession,intress,zila):
        self.profession=profession
        self.intress=intress
        self.zila=zila

    def details(self):
        print(self.profession,self.intress,self.zila)

    def compare(self,mahim):
        if self.profession==mahim.profession:
            print("same",mahim.profession)
        else:
            print("not same")
mahabub=name("programmer","coding","dinajpur")
bishal=name("student","watching football","saidpur")
bishal.details()
bishal.compare(mahabub)'''

class name:
    def __init__(self,post,thana,zila):
        self.post=post
        self.thana=thana
        self.zila=zila
    def view(self,para,division):
        self.para=para
        self.division=division
        print(para)
        print(division)




mahabub=["belaichandi","parbatipur","dinajpur"]
bishal=alam("black","green")