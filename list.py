cites = ["rawalpindi", "texila", "islambad", "abotabad", "mahsehra"]
print(cites)

print(cites[0])
print(cites[2])
print(cites[4])

numbers = [10,20,30]
numbers.append(40)
print(numbers)

numbers = [10, 20, 40, 50]
numbers.insert(2, 300)
print(numbers)

numbers.remove(50)
print(numbers)

cities = ["Rawalpindi", "Taxila", "Islamabad", "Abbottabad", "Mansehra", "Lahore"]
print(len(cites))

numbers = [10, 20, 30, 40, 50]
print(30 in numbers)


numbers = [12, 5, 18, 7, 20, 3, 25, 10]
a = 0
for i in numbers:
    if i > 10:
        print(i)
        a +=1

print(a)

numbers = [45, 12, 89, 3, 27, 10]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)

numbers = [45, 12, 89, 3, 27, 10]
numbers.sort()

print(numbers)



list = [
    ["Ali", 20],
    ["Ahmed", 25],
    ["Mehran", 39]
]

print(list[2][0])


numbers = [12, 45, 7, 89, 23, 56, 34]
j = 1
i = 0
g = 0
for i in range(len( numbers)):
    if numbers[i] > numbers[j]:
         g = numbers[i]
         break
    else:
        g = numbers[j]


print(g)
