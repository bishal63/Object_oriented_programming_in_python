#class variable toiri kori
'''class name:
    father_name=" "      #class variable
    def __init__(self,father_name):
        self.father_name=father_name
mahabub=name("muksadul")
alam=name("syed ali")
print(mahabub.father_name)
print(alam.father_name)'''

#instance method,static method ooo class method a class variable toiri kori
#instance class method a class variable
'''class name:
    father_name="muksadul"      #class  variable toiri korlam
    def __init__(self,age,school):
        self.age=age
        self.school=school

    def instance_method(self):
        print(self.father_name)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.instance_method()'''

#class method a class variable
'''class name:
    father_name="muksadul"
    def __init__(self,age,school):
        self.age=age
        self.school=school

    @classmethod                      #class method a class variable toiri korlam
    def class_method(self):
        print(self.father_name)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.class_method()'''


#static method a class variable toiri kori (static method a class variable ullekh kora jay na)
'''class name:
    father_name="muksadul"
    def __init__(self,age,school):
        self.age=age
        self.school=school

    @staticmethod  # static method toiri korlam (static_method ar parameter a kono attribute babohito hoy na)
    def static_method():
        print(self.father_name)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.static_method()           #static method a class variable ullekh kora jay na karon static method ar parameter a kichu ullekh kora thake na'''



#instance variable toiri kori
'''class name:
    father_name="muksadul"           #class variable
    def __init__(self,age,school):   #instance variable
        self.age=age
        self.school=school
    def instance_variable(self):
        print(self.age)
        print(self.school)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
alam.instance_variable()'''


#instance variable static method a babohar kori  (static_method ar parameter a kono attribute babohito na hoyay instance variable ullekh kora jay na)
'''class name:
    father_name="muksadul"           #class variable
    def __init__(self,age,school):   #instance variable
        self.age=age
        self.school=school

    @staticmethod  # static method toiri korlam (static_method ar parameter a kono attribute babohito na hoyay instance variable ullekh kora jay na)
    def static_method():
        print(self.age)
        print(self.school)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
alam.static_variable()'''

#class method a instance variable toiri kori
'''class name:
    father_name="muksadul"           #class variable
    def __init__(self,age,school):   #instance variable
        self.age=age
        self.school=school
    def class_variable(self):      #class variable toiri korlam
        print(self.age)
        print(self.school)
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
alam.class_variable()'''

