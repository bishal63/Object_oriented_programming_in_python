#jokhon kono method nijer name variable ba class variable charaw onno class ar name variable ba class variable babohar kore tokhon take method overriding bole

#inheritance babohar kore method overriding kora hoy
class muksadul:
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def all1(self):
        print(self.father_name)
        print(self.mother_name)
        print("sonapukur")
    def profession1(self):
        print("farmer")
    def shop1(self):
        print("stationary")
class mahabub(muksadul):
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name
    def all(self):
        print(self.father_name)
        print(self.mother_name)
        print("dinajpur")
    def profession(self):    #polymorphism toiri korlam (duita vinno class akoi namer function use korlam)
        print("student")
    def shop(self):
        print("plaza")
muksadul1=muksadul("syedali","moslema")
mahabub1=mahabub("muksadul","mahafuja")

mahabub1.shop()
mahabub1.shop1()        #inherit kore mahabub class charaw mahabub class ar object babohar kore muksadul class ar method overriding korlam
mahabub1.all()
mahabub1.all1()         #inherit kore mahabub class charaw mahabub class ar object babohar kore muksadul class ar method overriding korlam
mahabub1.profession()
mahabub1.profession1()   #inherit kore mahabub class charaw mahabub class ar object babohar kore muksadul class ar method overriding korlam