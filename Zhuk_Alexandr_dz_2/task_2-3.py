my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
print(id(my_list), my_list)

while i < len(my_list):
    item_len = ''
    item = my_list[i]
    if item[-1].isdigit():
        my_list.insert(i, '"')
        i += 1
        str_len = 3 if item.startswith(('+', '-')) else 2
        if len(item) < str_len:
            item = item.zfill(str_len)
            my_list[i] = item
        i += 1
        my_list.insert(i, '"')
    i += 1

print(id(my_list), " ".join(my_list))

