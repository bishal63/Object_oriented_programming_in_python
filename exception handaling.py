'''file=open("object oriented programming.py","r")
print(file.read())
file.close()'''

'''try:
    file=open("mahabub.py","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("[Errno 2] No such file or directory: 'mahabub.py'")'''

try:
    def mahabub(a, b):
        print(a/b)
    mahabub(10,0)
except ZeroDivisionError:
    print("division by zero")

