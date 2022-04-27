def price(list, text):
    print(f'\n{id(list)} - {text}')
    for i in list:
        print(f"{int(i)} руб. {int(i * 100 % 100):02} коп.", end=", ")
    return

my_list = [57.8, 46.51, 97, 12.03, 0.11, 68.47, 100.34, 5.19, 491.99, 1, 26.37, 37.11]

print(price(my_list, 'Преобразованный список: '))

my_list.sort()
print(price(my_list, 'Отсортированный список по возрастанию: '))
print(price(my_list[-5:], 'Список 5 самых дорогих товаров: '))

new_list = sorted(my_list, reverse=True)
print(price(new_list, 'Отсортированный список по убыванию: '))