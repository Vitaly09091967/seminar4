# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она 
# растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко 
# времени сбора на них выросло различное число ягод — на i-ом кусте выросло 
# ai ягод. В этом фермерском хозяйстве внедрена система автоматического 
# сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с 
# двух соседних с ним. Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки.

import random
n = int(input("введите количество кустов: "))
berries = list(random.randint(0, 10) for i in range(n))
print(berries)
max_berries = 0
for i in range(1, n - 1): 
    curr_berries = berries[i] + berries[i-1] + berries[i+1]    
if curr_berries > max_berries:
    max_berries = curr_berries
        
print("Максимальное количество ягод, которое можно собрать за один заход:", max_berries)



