#akoi namer function vinno vinno class jodi vinno vinno kaj kore tahole take polymorphism bole

#polymorphism toi kori
class muksadul:
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def all(self):
        print(self.father_name)
        print(self.mother_name)
        print("sonapukur")
    def profession(self):
        print("farmer")
class mahabub:
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name
    def all(self):
        print(self.father_name)
        print(self.mother_name)
        print("dinajpur")
    def profession(self):    #polymorphism toiri korlam (duita vinno class akoi namer function use korlam)
        print("student")
muksadul1=muksadul("syedali","moslema")
mahabub1=mahabub("muksadul","mahafuja")
#muksadul1.all()
#mahabub1.all()
muksadul1.profession()
mahabub1.profession()    #polymorphism toiri korlam (vinno class a akoi namer duita use korlam ooo duitay vinno kaj korlo
