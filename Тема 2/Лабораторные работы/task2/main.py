list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение 5-го по порядку элемента средним арифметическим
sum_ = sum(list_numbers)
len_ = len(list_numbers)
average_ = (sum_ / len_)
list_numbers[4] = average_

print(list_numbers)