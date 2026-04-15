#21-misol
shaxs = {"ism": "Jamshid", "yosh": 21, "shahar": "Xorazm"}
print(shaxs)
shaxs.setdefault("kasb", "Talaba")
print(shaxs)

#22-misol
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

dict1.update(dict2)
dict1.update(dict3)
print(dict1)

#23-misol
talaba = {
    "ism": "Nodira",
    "familiya": "Rahimova",
    "yosh": 20,
    "kurs": 3,
    "fakultet": "Dasturiy injiniring",
    "stipendiya": True
}

#24-misol
narxlar = {
    "Non": 3000,
    "Sut": 9000,
    "Tuxum": 18000,
    "Go'sht": 85000,
    "Yog'": 45000,
    "Sabzi": 7000
}
print(narxlar["Go'sht"])

#25-misol
matn = "salom dunyo salom python python python dunyo"
soz = matn.split()
natija = {}

for soz in soz:
    if soz in natija:
        natija[soz] += 1
    else:
        natija[soz] = 1

print(natija)

#1-misol
numbers = [12, -5, 7, -3, 0, 25, -11, 8]
print(numbers)

for el in numbers[:]:
    if el < 0:
        numbers.remove(el)

print(numbers)

#2-misol
numbers = [45, 12, 78, 3, 56, 89, 23]
katta = max(numbers)
print("Eng katta son:",katta)

kicci = min(numbers)
print("Eng kichik son:",kicci)

#3-misol
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[::-1])

#4-misol
numbers = [14, 7, 22, 9, 31, 18, 5]

#5-misol
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print()
list3 = list1 + list2
print(list3)

list3 = set(list3)
print(list3)

list3 = list(list3)
print(list3)

#6-misol
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))

#7-misol
numbers = [5, 3, 7, 3, 9, 3, 1]
print(numbers.count(3))

#9-misol
numbers = [29, 10, 14, 37, 13]

numbers.sort(reverse=False)
print(numbers)

#10-misol
numbers = [4, 6, 2, 6, 8, 4, 6, 2]
print(numbers.count(6))

#11-misol
words = ["python", "java", "c++", "golang"]
print(words)

words = [word.upper() for word in words]

print(words)

#13-misol
numbers = [100, 200, 300, 400]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

#14-misol
roy = []
for i in range(6):
    x = int(input("son kiriting: "))
    if x >= 0:
        roy.append(x)

print(roy)

#15-misol
words = ["apple", "banana", "kiwi", "strawberry"]
m = max(words, key=len)
print(m)
