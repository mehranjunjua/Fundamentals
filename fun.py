def add(a , b):
    print(a+b)

add(10,20)

def greet(name="Mehran"):
    print("Hello", name)


greet("Ali")


try:
    a = int(input("enter number "))
    print(a)
except ValueError:
    print("Please enter a valid numberas")


def check_age(age):
    try:
        if age < 18:
            raise ValueError("Age must be 18 or older")
        print("Access granted")

    except ValueError as error:
        print(error)


check_age(15)


a = {10,20,20,30,40,40,50}

a.add(60)

print(a)