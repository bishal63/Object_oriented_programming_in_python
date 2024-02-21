class muksadul:
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def profession(self):
        print(self.father_name)
        print(self.mother_name)
        print("sonapukur")

    class son_mahabub(muksadul):    #nested class toiri korlam (class ar vitor class toiri korlam)
        def __init__(self,father_name,mother_name):
            self.father_name = father_name
            self.mother_name = mother_name

        def profession1(self):
            print(self.father_name)
            print(self.mother_name)
            print("dinajpur")

class mahfuj(muksadul):
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def address(self):
        print(self.father_name)
        print(self.mother_name)
        print("parbotipur")
    class mahim(muksadul.son_mahabub):
        def __init__(self, father_name, mother_name):
            self.father_name = father_name
            self.mother_name = mother_name

        def address(self):
            print(self.father_name)
            print(self.mother_name)
            print("parbotipur")
mahfuj1=mahfuj("a","b")
mahim1=mahfuj1.mahim("c","d")
muksadul1=muksadul("syedali","moslema")
son_mahabub1=muksadul1.son_mahabub("muksadul","mahafuja")
#mahim1.address()
#mahfuj1.address()
#muksadul1.profession()
#son_mahabub1.profession1()
mahim1.profession1()
print(muksadul1.son_mahabub)
#mahim1.address()
#mahfuj1.address()
#muksadul1.profession()
#son_mahabub1.profession1()



