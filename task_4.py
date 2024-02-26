import csv
'''
Импорт библиотеки csv для работы с файлом
'''
def promo(row):
    '''Функция для создания промокода
    row - строка со значениями товара
    '''
    number, month = (row['Date'].split('.'))[:2]
    ## Получаем число и месяц из row['Date']
    promokod = (row['product'].upper())[:2] + number + (row['product'].upper())[:-3:-1] + month[::-1]
    ## Составляем промокод по алгоритму из первых 2-ух букв названия + день поступления +
    ## 2 предпоследних буквы названия в обратном порядке + месяц поступления в обратном порядке
    return promokod ## Возвращаем промокод в виде строки


with open('products.csv', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter = ';'))
    ## Открываем файл и записываем значения в переменную data
    ## В ввиде списка в котором каждый элемент имеет ключ и значение
    for row in data:
        ## Создаем новый столбец с промокодами для товаров
        row['promocode'] = promo(row)

with open('product_promo.csv', 'w', encoding='utf-8-sig', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    ## Создаем новый файл так как 2 элемент в open() это 'w' то есть запись
    ## Записываем заголовки как было в прошлом файле плюс новый total
    writer.writeheader()
    writer.writerows(data)
    ## Записываем значения
