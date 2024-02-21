#class and method toiri koron
'''class student:
    name1="mahabub"
    name2="alam"

    def school():
        print("sunflower school and college")

print(student.name1)
print(student.name2)
student.school()'''

'''class student:
    name1=""
    name2=""

    def school():
        print("sunflower school and college")

student.name1=("mahabub")
student.name2=("alam")
#print(student.name1)
#print(student.name2)
#student.school()
print(dir(student))'''

#constractor method diye class oo object toiri kori
class car:
    def __Init__(self,name,department):
        self.name=name
        self.deprtment=department

    def start(self):
        print("sunflower school and college")

car_1=car("mahabub","computer")
car_2=car("jannat","civil")
print(car_2.name)