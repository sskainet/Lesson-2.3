my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len(my_list):
    current_element = my_list[num]
    if current_element < 0:
        break
    if current_element > 0:
        print(current_element)
    num += 1