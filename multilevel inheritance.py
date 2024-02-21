class baba:
    taka="1 crore"
    car="toyota"
    home="3 floor"

class baba2(baba):
    camera="canan"
    soil="1 bigha"
    sofa="2 ta"
class baba3(baba2):
    house="3 ta"
    cycle="hero"
    motor="r15"
class child(baba3):
    phone:"oppo"
    laptop="hp"

k=child()

print(k.cycle)
print(k.camera)