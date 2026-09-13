student = {"name" : "Mehran",
            "age" : "39",
            "city" : "Rawalpindi",
            "job" :"Python Developer"}

print(student)

print(student["name"])

student["gender"] = "male"
student["age"]  = 29

print(student)

print(student.get("abc", "all or nothing"))

for key, Value in student.items():
    print(key, Value)


for value in student.values():
    print(value)



students = {
    "Ali": 78,
    "Ahmed": 45,
    "Mehran": 92,
    "Usman": 61
}

for key in students.keys():
    if students[key] > 60:
        print(key)