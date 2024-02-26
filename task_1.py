import csv
'''
Импорт библиотеки csv для работы с файлом
'''
with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter = ';'))
    ## Открываем файл и записываем значения в переменную data
    ## В ввиде списка в котором каждый элемент имеет ключ и значение
    for row in data:
        row['total'] = float(row['Price per unit'])*float(row['Count'])
        ##Для каждой строки в data записываем в новый столбец total значение выражения
    summary = 0
    for row in data:
        if 'Закуски' in row['Category']:
            summary += int(row['total'])
            ## Если категория "Закуски", то прибавляем к переменной summary
print(summary)
## Выводим итоговую сумму для категории закуски

with open('products_new.csv', 'w', encoding='utf-8-sig', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    ## Создаем новый файл так как 2 элемент в open() это 'w' то есть запись
    ## Записываем заголовки как было в прошлом файле плюс новый total
    writer.writeheader()
    writer.writerows(data)
    ## Записываем значения
