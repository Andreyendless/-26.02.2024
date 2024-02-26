import csv
'''
Импорт библиотеки csv для работы с файлом
'''
with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter = ';'))
    ## Открываем файл и записываем значения в переменную data
    ## В ввиде списка в котором каждый элемент имеет ключ и значение
    for i in range(len(data)):
        ## Алгоритм сортировки вставками (Сортировка по кол-ву проданных товаров по возрастанию)
        cursor = data[i]
        cursor_score = float(cursor['Count'])
        pos = i
        while pos > 0 and float(data[pos-1]['Count']) > cursor_score:
            data[pos] = data[pos-1]
            pos -= 1
        data[pos] = cursor
    for i in range(len(data)):
        ## Алгоритм сортировки вставками (Для сортировки по категориям)
        cursor = data[i]
        cursor_category = cursor['Category']
        pos = i
        while pos > 0 and cursor_category < data[pos-1]['Category']:
            data[pos] = data[pos-1]
            pos -= 1
        data[pos] = cursor
    category_input = input()
    ## Получаем значение категории
    while category_input != 'молоко':
        ## Проверка что это не молоко
        for row in data:
            if category_input == row['Category']:
                ## Ищем первый элемент в категории так как у него наименьшее кол-во продаж
                print(f'В категории: {row["Category"]} товар: {row["product"]} был куплен {row["Count"]} раз')
                ## Останавливаем поиск так как элемент нашли и ждем ввода новой категории
                break
        else:
            ## Если не нашлось то пишем это
            print('Такой категории не существует в нашей БД')
        category_input = input()
        ## Снова вводим категорию
