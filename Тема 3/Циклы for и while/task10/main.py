list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]
count = 0  # чет
count_ = 0  # нечет
for even in list_:
    if even % 2 == 0:
        count += 1
    else:
        count_ += 1
if count > count_:
    print("Четных чисел больше")
elif count < count_:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")



# TODO завести отдельные счетчики для четных и нечетных чисел

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

# TODO вывести каких чисел больше
