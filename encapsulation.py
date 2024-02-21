#public and priat encapsulations

'''class student:
    def __init__(self,name,roll):
        self.name=name      #public encapsulations
        self.roll=roll      #public encapsulations
        self.__roll=roll    #privat encapsulations
    def view(self):
        print("name:",self.name,"roll:",self.__roll)

student1=student("mahabub",1234)
student2=student("bishal",7654)
print(student1.name)       #public encapsulations
print(student2.__roll)     #privat encapsulations
#print(student1.roll)
student2.view()'''


#privet encapsulations update
'''class student:
    def __init__(self,name,roll):
        self.name=name      #public encapsulations
        self.roll=roll      #public encapsulations
        self.__roll=roll    #privat encapsulations
    def view(self):
        print("name:",self.name,"roll:",self.__roll)

    def update_roll(self,roll):
        if (roll>0):
            self.__roll=roll
        else:
            print("no id")

student1=student("mahabub",1234)
student2=student("bishal",7654)

student1.update_roll(-123)
student1.view()
student2.view()'''


#update privet encapsulations exercise
'''class peapole:
    def __init__(self,name,village,zila):
        self.name=name
        self.village=village
        self.zila=zila
        self.__zila=zila
    def view(self):
        print(self.name,self.village,self.__zila)

    def update_zila(self,zila):
        if (zila=="rangpur"):
            self.__zila=zila
        else:
            print("error")


peapole1=peapole("mahabub","sonapukur","dinajpur")
peapole2=peapole("bishal","saidpur","nilphamari")

print(peapole1.zila)
peapole1.update_zila("rangpur")

peapole1.view()
peapole2.view()'''


#get set method ar maddhome encapsulations update

'''class name:
    def __init__(self,father,mother):
        self.mother=mother
        self.__father=father
    def view(self):
        print("father name:",self.__father,"mother name:",self.mother)

    def set_father(self,father):
        self.__father=father
    def get_father(self):
        return self.__father


mahabub=name("muksadul","mahfuja")
saikat=name("manik","swapna")
mahabub.view()
saikat.view()
#saikat.set_father("shafiqul")
#print(saikat.get_father())
#saikat.view()'''

#encapsulations attribute privet

class name:
    def __init__(self,zila,village):
        self.zila=zila
        self.village=village
    def view(self):
        print(self.zila,self.village)
        self.__method()
    def __method(self):
        print("ami tomay valobashi")


mahabub=name("dinajpur","sonapukur")
hridita=name("nilphamari","saidpur")
mahabub.view()
#mahabub.__method()