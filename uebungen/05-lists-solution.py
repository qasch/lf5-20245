# Übung 1
fruits = ["apple", "banana", "strawberry", "pineapple", "raspberry"]
print(f"Letzes Element: {fruits[len(fruits) - 1]}")
print(f"Letzes Element: {fruits[-1]}")
print(f"Zweites Element: {fruits[1]}")

# Übung 2
# index   0  1  2  3  4  5  6  7  8  9
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Die ersten fünf Zahlen: {zahlen[:5]}")
print(f"Die letzten drei Zahlen: {zahlen[-3:]}")

# Übung 3
numbers = []
# numbers = list()   # auch möglich

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# Würde auch so gehen (besser!)
# for x in range(6):
#     numbers.append(x)
# print(numbers)

numbers.remove(3)
numbers.pop(1)

print(numbers)


# Übung 6
names = ["Karl", "Berta", "Lisa", "Grunhilde"]
name_to_find = "Grunhilde"

if names.count(name_to_find) == 1:
    print(f"{name_to_find} ist in der Liste enthalten")
else:
    print(f"{name_to_find} ist *nicht* in der Liste enthalten")

# besser, falls der Name mehr als einmal in der Liste vorkommt
if names.count(name_to_find) > 0:
    print(f"{name_to_find} ist in der Liste enthalten")
else:
    print(f"{name_to_find} ist *nicht* in der Liste enthalten")

# kurze, sprechende Schreibweise in Python mit dem "in" Operator
if name_to_find in names:
    print(f"{name_to_find} ist in der Liste enthalten")
else:
    print(f"{name_to_find} ist *nicht* in der Liste enthalten")


# Übung 7
some_numbers = [24, 111, 42, 6, 17, 4, 1]

my_sum = 0
for element in some_numbers:
    my_sum = my_sum + element
average = my_sum / len(some_numbers)
print(average)

average = sum(some_numbers) / len(some_numbers)
print(average)


# Übung 8
list1 = ["eins", "zwei", "drei"]
list2 = ["vier", "fünf", "sechs"]

combined_lists = list1 + list2
print(combined_lists)

# auch möglich
list1.extend(list2)
print(list1)

# Vorsicht: hier wird die list2 als ein Element als Liste angefügt
list1.append(list2)
print(list1)

# Übung 9
# index   0  1  2
zeile1 = [1, 2, 3]
zeile2 = [4, 5, 6]
zeile3 = [7, 8, 9]

# index     0       1        2
matrix = [zeile1, zeile2, zeile3]

# index       0          1          2
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

print(zeile2[2])
print(matrix[1][2])

# Ausgabe aller Element der Matrix
for row in matrix:
    for column in row:
        print(column, end=" ")
print("Ende")
