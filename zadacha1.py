# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, 
# с повторениями). Выдать без повторений в порядке возрастания все те 
# числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа.
# n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
Set1 = set()
Set2 = set()
for i in range(n):
    elem = int(input(f"Введите элемент {i + 1} первого множества: "))
    Set1.add(elem)
for i in range(m):
    elem = int(input(f"Введите элемент {i + 1} второго множества: "))
    Set2.add(elem)
intersection = sorted(Set1.intersection(Set2))
print("Числа, которые встречаются в обоих множествах: ")
for elem in intersection:
    print(elem)