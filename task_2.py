import csv
'''
Импорт библиотеки csv для работы с файлом
'''
with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter = ';'))
    ## Открываем файл и записываем значения в переменную data
    ## В ввиде списка в котором каждый элемент имеет ключ и значение
    for i in range(len(data)):
        ## Алгоритм сортировки вставками (Сначала сортируем по значениям цены)
        cursor = data[i]
        cursor_score = float(cursor['Price per unit'])
        pos = i
        while pos > 0 and float(data[pos-1]['Price per unit']) < cursor_score:
            data[pos] = data[pos-1]
            pos -= 1
        data[pos] = cursor
    for i in range(len(data)):
        ## Алгоритм сортировки вставками (Затем сортируем по категориям в алфавитном порядке)
        cursor = data[i]
        cursor_category = cursor['Category']
        pos = i
        while pos > 0 and cursor_category < data[pos-1]['Category']:
            data[pos] = data[pos-1]
            pos -= 1
        data[pos] = cursor
    ## Создаем массив в который будем записывать категории товаров
    category = set()
    for row in data:
        ## Так как первая строчка в категории имеет максимальную цену,
        ## то выведем её и пропустим все остальные товары из этой категории
        if row['Category'] not in category:
            ## Для сокращения места записал длинные строки в отдельные переменные и вывел их позже
            x, y, z = 'В категории:','самый дорогой товар:','его цена за единицу товара составляет'
            print(f'{x} {row["Category"]} {y} {row["product"]} {z} {row["Price per unit"]}')
            category.add(row['Category'])
            ## Добавляем в массив что-бы перейти к следующей категории
