'''je class ar kono object toiri kora hoy na kintu class ar method gulor acccess newa jay,tader
ke muloto abstraction bole'''
'''from abc import ABC,abstractmethod   #abstract  method import kori
class muksadul(ABC):        #je class a babohar korbo se class a abstract inherit kori
    @abstractmethod
    def school(self):     #je method ar abstract korte hobe se method ar print function babohar kora jabe na (child class a ta babohar korte hobe)
        pass
    @abstractmethod       #je method ar abstract korte hobe se method ar print function babohar kora jabe na (child class a ta babohar korte hobe)
    def study(self):
        pass
    def bazar(self):      #concreate abstraction toiri korlam
        print("bazar korte hobe")
class mahabub(muksadul):
    def school(self):
        print("school jaite hobe")     #abstract kora method ke child class a babohar korte hobe
    def study(self):                   #abstract kora method ke child class a babohar korte hobe
        print("boi porte hobe")
    def sports(self):
        print("ball khelbo")
    def friend(self):
        print("adda dibo")

mahabub1=mahabub()
mahabub1.sports()
mahabub1.friend()
mahabub1.study()        #abstraction toiri korlam
mahabub1.school()       #abstraction toiri korlam
mahabub1.bazar()        #concreate abstraction'''



from abc import ABC,abstractmethod
class muksadul(ABC):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def school(self):
        pass

class mahabub(muksadul):
    def study(self):
        print("boi porte hobe")
    def school(self):
        print("school jaite hobe")
    def __init__(self,sports,adda):
        self.sports=sports
        self.adda=adda
    def all(self):
        print(self.sports)
        print(self.adda)
    def bazar(self):
        print("taka mara")
mahabub1=mahabub("football","friends party")
mahabub1.all()
mahabub1.bazar()
mahabub1.study()
mahabub1.school()




