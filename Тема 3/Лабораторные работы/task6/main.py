list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = list_numbers[0]
for i in range(len(list_numbers)):
        if i > max_index:
            max_index += i
            max_index, list_numbers[-1] = list_numbers[-1], max_index



print(list_numbers)
print(max_index)
print(list_numbers[-1])
print()
