import csv
'''
Импорт библиотеки csv для работы с файлом
'''
with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter = ';'))
    ## Открываем файл и записываем значения в переменную data
    ## В ввиде списка в котором каждый элемент имеет ключ и значение
    hashe = {}
    ## Создаём словарь
    for row in data:
        hashe[row['Category']] = hashe.get(row['Category'], 0) + float(row['Count'])
        ## Перемещаем в словарь общее кол-во товаров из категории
    ## Теперь в словаре находятся ключи в виде категорий товаров и значения в виде общего
    ## кол-ва товаров из данной категории
    hasha = [[row, int(float(hashe[row]))] for row in hashe]
    ## Создаем Список для удобства сортировки и вывода данных
    ## И сортируем его по второму элементу, то есть кол-ву проданных товаров
    hasha = sorted(hasha, key = lambda x: x[1])
    ## Создаём счётчик
    count = 0
    for row in hasha:
        ## Пока счётчик не привысил числа 10
        if count < 10:
            count += 1
            ## Выводим Название категории и кол-во проданного товара из этой категории
            print(f'{row[0]}, {row[1]}')