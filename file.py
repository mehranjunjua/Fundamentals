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


with open("name.txt","w+") as file:
    file.write("Mehran Junjua")
    file.seek(0)
    print(file.read())
    print(file.tell())
    file.seek(5)
    print(file.tell())


def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def hello():
    print("Helloo Mehran")

hello = my_decorator(hello)



def gril(x):
    def mf():
        print("Good ha g")
        x()
        print("no tanks")
    return mf


@gril
def hy():
    print("hi g")

hy()



class MyFile:
    def __enter__(self):
         print("File Opened")

    def __exit__(self, exc_type, exc, tb):
         print("File closed")

with MyFile():
     print("Working with file")

     
def multiply(a : int, b: int) -> int: 
        return a * b



numbers = [10, 25, 7, 40, 18, 3]
a = 1
for i in numbers:
    if i > numbers[a]:
        large = i

for i in numbers: 
    if i < numbers[a]:
        small = i

for i in numbers: 
    sum += i

avg = sum / 6

print(large, small, sum, avg )



numbers = [12, 5, 8, 12, 20, 5, 3, 20, 8]

unique = []

for i in numbers:
    if i not in  unique:
        unique.append(i)


print(unique)

"""
text = "Python is easy and Python is powerful"

words = text.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)