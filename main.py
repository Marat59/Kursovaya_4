from src.helper import search
from src.helper import search_by_criteria

f = 0
while f != 10:
    try:
        a = input('Введите 1 для поиска по названию, 2 для поиска по описанию (По умолчанию 1): ')
        if not (a in ['', '1', '2', '3']):
            print('Введите корректный номер для начала поиска')
        if a == '1' or a == '':
            search()
            print()
        elif a == '2':
            search_by_criteria()
            print()
    except:
        f += 1
        print('Введен некорректный номер \n')
