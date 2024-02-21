#single inheritange
'''class baba:
    taka="1 crore"
    car="toyota"
    home="3 floor"

class child(baba):
    phone:"oppo"
    laptop="hp"

k=child()

print(k.taka)'''

#single inheritange make kori

'''class father:
    def __init__(self,name,occupation):
        self.occupation=occupation
        self.name=name
    def live(self):
        print("live in bangladesh")

class son(father):
    def mahim(self):
        print("ami tomay valobashi")
        print("i love you")

father1=father("muksadul","farmer")
son1=son("mahabub","student")
son1.mahim()
father1.live()
son1.live()
father1=mahim()    #inheritange kaj korbe na'''

#multilevel inheritange make kori
'''class mahabub:
    car="mercidies"
    camera="canon"
    phone="oppo"
class alam(mahabub):
    home="duplex"
    laptop="hp"
    bike="r15"
class bishal(alam):
    study="nsu"
    job="america"
    play="football"

name1=mahabub()
name2=alam()
name3=bishal()
print(name3.phone)
print(name2.car)
#print(mahabub.study)     #multilevel inheritange kaj korbe na'''

#multilevel inheritange make kori
'''class mahabub:
    def __init__(self,college,department):
        self.college=college
        self.department=department
    def password(self):
        print(13245)
class alam(mahabub):
    def session(self):
        print("2022-2023")
class bishal(alam):
    def id(self):
        print(1426)

name1=mahabub("aiub","eee")
name2=alam("diu","ce")
name3=bishal("du","cse")
name3.session()
name3.password()
name3.id()
name2.password()
#name2.id()     #multilevel inheritange kaj korbe na'''

#multiple inheritange make kori
'''class muksadul:
    place="2 bigha"
    taka="1 crore"
    home="3 floor"
class manik:
    job="interpreneur"
    car="audi"
    bike="ktm"
class mahabub(muksadul,manik):
    girlfriend="12 ta"
    camera="canon"
    phone="iphone"
name1=mahabub()
name2=manik()
name3=muksadul()
print(name1.home)
print(name1.bike)
print(name1.phone)
#print(name3.phone)         #multiple inheritange kaj korbe na
print(name2.camera)         #multiple inheritange kaj korbe na'''

#multiple inheritange make kori
'''class muksadul:
    def __init__(self):
        print("dif kora holo")
    def method1(self):
        print("ami baper boro chele")
class manik:
    def job(self):
        print("govment employe")
    def method2(self):
        print("ami baper majo chele")
class mahabub(muksadul,manik):
    def __init__(self):
        #super().__init__()
        #manik.__init__(self)
        print("init of c")
    def method3(self):
        print("ami muksadul ar chele")
name3=mahabub()
name2=manik()
#name1=muksadul()
#name2=manik()
name3.method2()
manik.method2(mahabub)
name2.method3()    #multiple inheritange kaj korbe na'''

#hierarchical inheritange make kori
'''class muksadul:
    land="2 bigha"
    home="3 ta"
    car="audi"
class mahabub(muksadul):
    study="polytechnic"
    phone="oppo"
    laptop="hp"
class mahim(muksadul):
    cow="2 ta"
    cycle="hero"
    bike="r15"
name1=mahabub()
name2=mahim()
name3=muksadul()
print(name1.car)
print(name2.land)
print(name3.phone)     #hierarchical inheritange kaj korbe na
print(name3.cow)       # #hierarchical inheritange kaj korbe na'''

#hierarchical inheritange make kori
'''class student:
    def __init__(self,name,id,password):
        self.name=name
        self.id=id
        self.password=password
    def campus(self):
        print("wonderful environment")
class csestudent(student):
    def __init__(self,name,id,password,labs):
        super().__init__(name,id,password)
        self.labs=labs
    def cry(self):
        print("all day study")
class bbastudent(student):
    def party(self):
        print("all dat party")
student1=csestudent("mahabub",11,475,3)
student2=bbastudent("mahim",22,908)
student1.cry()
student2.campus()
student1.campus()
student2.cry()          #hierarchical inheritange kaj korbe na
student1.party()         #hierarchical inheritange kaj korbe na'''

#inheritange ar variable overriding
'''class student:
    def __init__(self,name):
        self.name=name
        self.course="phitron"          #value add kora acce
    def campus(self):
        print("use everybody")
class cse_student(student):
    def __init__(self,name,course):        #course ta variable overridding
        super().__init__(name)
        self.course=course
    def lab(self):
        print("cry everytime")
class bba_student(student):
    def enjoy(self):
        print("chill everytime")

name1=cse_student("mahabub","bohubiri")
name2=bba_student("rofiq")
print(name1.__dict__)
print(name2.__dict__)
name1.lab()
name2.enjoy()
name2.lab()            #inheritange kaj korbe na
name1.enjoy()           #inheritange kaj korbe na'''

#inheritance method overridding
'''class muksadul:
    def __init__(self):
        print("__init__ of class muksadul")
    def method1(self):
        print("you will get all of my property")
    def method2(self):
        print("some study")
class mahabub(muksadul):
    def __init__(self):
        pass
        #print("__init__ of class mahabub")
    def method1(self):        #method overridding kora hoy method ar name akoi rakhe
        super().method1()
        print("party always")
name1=mahabub()
name1.method1()
name1.method2()'''

#inheritance method overridding exercise
class muksadul:
    def __init__(self):
        print("__init__of class muksadul")
    def advice1(self):
        print("some study")
    def advice2(self):
        print("you will get all off my properties")
class mahabub(muksadul):
    def __init__(self):
        pass
        #print("__init__ of class mahabub")
    def advice1(self):
        super().advice1()
        print("always party")

name1=mahabub()
name1.advice1()
name1.advice2()
