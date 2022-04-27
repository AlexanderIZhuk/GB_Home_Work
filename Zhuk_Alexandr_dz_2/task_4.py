my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in my_list:
    list_name = el.split(' ')[-1].capitalize()
    print(f'Привет, {list_name}!')
