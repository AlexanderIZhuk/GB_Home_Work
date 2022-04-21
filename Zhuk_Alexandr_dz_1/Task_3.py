for i in range(1, 101):
    if i % 10 > 4 and i % 10 <= 10 or i % 10 == 0 or i > 10 and i < 20:
        print(i, "Процентов")
    elif i % 10 > 1 and i % 10 < 5 :
        print(i, "Процента")
    elif i % 10 == 1:
        print(i, "Процент")