for x in range(1, 1000, 2):
    cube_list = x**3
    cube_sum = 0
    number_one = cube_list
    while number_one != 0:
        number = number_one % 10
        cube_sum = int(cube_sum) + number
        number_one = number_one // 10
    if cube_sum % 7 == 0:
        print("Ссума чисел делящихся на 7 : ", cube_sum)
    # Часть b
    cube_list_b = cube_list + 17
    cube_sum_b = 0
    number_one_b = cube_list_b
    while number_one_b != 0:
        number_b = number_one_b % 10
        cube_sum_b = int(cube_sum_b) + number_b
        number_one_b = number_one_b // 10
    if cube_sum_b % 7 == 0:
        print("(Часть b) Ссума чисел делящихся на 7 : ", cube_sum_b)