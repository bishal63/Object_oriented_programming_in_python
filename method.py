#instance method toiri kore class toiri kori
'''class name:
    father_name="muksadul"
    def __init__(self,age,school):
        self.age=age
        self.school=school
    def instance_method(self):     #instance method toiri kore notun class toiri korlam
        print("I love programming")
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
alam.new_method()               #instance method a object ke dhore call korte hoy
#name.new_method()              #instance method a class  ke dhore call kora jay na tahole error dekhay'''


#class method toiri kore class toiri kori
'''class name:
    father_name="muksadul"
    def __init__(self,age,school):
        self.age=age
        self.school=school
    def instance_method(self):     #instance method toiri kore notun class toiri korlam
        print("I love programming")
    @classmethod                #class method toiri korlam
    def class_method(self):
        print("notun class toiri korlam")
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
name.class_method()             #class method ke class dhore call kora jay
mahabub.class_method()          #class method ke abar object dhorew call kora jay'''


#static method toiri kore class toiri kori
'''class name:
    father_name="muksadul"
    def __init__(self,age,school):
        self.age=age
        self.school=school
    def instance_method(self):     #instance method toiri kore notun class toiri korlam
        print("I love programming")
    @classmethod                #class method toiri korlam
    def class_method(self):
        print("notun class toiri korlam")
    @staticmethod              #static method toiri korlam (static_method ar parameter a kono attribute babohito hoy na)
    def static_method():
        print("I am a future programmer of Bangladesh")
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.static_method()       #static method ke object dhore call kora jay
name.static_method()          #static method ke class dhorew call kora jay'''