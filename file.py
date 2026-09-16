"""

file = open("notes.txt", "w")

file.write("I am going to become a Python backend developer")

file.close()

file = open("class.txt", "w")

file.write("This file name is class")

file.close()


file = open("notes.txt", "r")
print(file.read())
file.close()



with open("class.txt", "w+") as file:
    file.write("alif , bay batowa, bili marya chowa")
    file.seek(0)
    print(file.read())

"""
with open("name.txt","w+") as file:
    file.write("Mehran Junjua")
    file.seek(0)
    print(file.read())
    print(file.tell())
    file.seek(5)
    print(file.tell())