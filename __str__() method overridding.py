'''class student:
    def __init__(self,name,zila):
        self.name=name
        self.zila=zila
        #print(self)
    def __str__(self):
        return "my name is " +  self.name


student1=student("mahabub","dinajpur")
student2=student("bishal","nilphamari")
print(student1)
print(student2)
#print(student1.__str__())
#print(student2.__str__())'''



#__str__() method overridding exercise
#use kora hoy muloto memory location name print na kore variable information print korte

class name:
    def __init__(self,divison,distric):
        self.divison=divison
        self.distric=distric
        print(self)
    def __str__(self):
        return "there zila name is " + self.divison

name1=name("rangpur","dinajpur")
name2=name("dhaka","nilphamari")