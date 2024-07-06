from src.hhsaver import HHsaver
from src.hh import HH

def save(answer_list_of_vacs):
    exm = HHsaver()
    exm.vacancy_add(answer_list_of_vacs)

def search():
    flag = True
    while flag == True:
        req = input('Введите название вакансии: ').title().strip() #заглавная и строчные + убрать пробелы по бокам
        a = HH('file_worker') #создали экз HН, чтобы было с чем работать
        try:
            print('Информация загружается...\n')
            a.load_vacancies(req)  # по ключевому слову получаем список ваквак
            answer_list_of_vacs = a.get_vacs()
            save(answer_list_of_vacs)
            if len(answer_list_of_vacs) == 0:
                print('Вакансии не найдены\n')
            else:
                for elem in answer_list_of_vacs:
                    print(elem)
                    flag = False
                print("\nХотите вывести топ вакансий по зп в рублях? Если не хотите - 0. ")
                count = int(input('Введите кол-во: '))
                print()
                if count != 0:
                    result = a.get_top_vacancies_by_salary(count, answer_list_of_vacs)
                    for i in result:
                        print(i)
        except:
            print('Введите корректный запрос!\n')


def search_by_criteria():
    flag = True
    while flag == True:
        req = input('Введите ключевое слово для поиска в описании: ').title().strip()  # заглавная и строчные + убрать пробелы по бокам
        a = HH('file_worker')  # создали экз HН, чтобы было с чем работать
        try:
            print('Информация загружается...\n')
            a.load_vacancies(req)  # по ключевому слову получаем список ваквак
            b = a
            answer_list_of_vacs = a.get_vacs()
            save(answer_list_of_vacs)
            flg = True
            for vac in answer_list_of_vacs:
                a = vac.get_description()
                if a == None:
                    a = ''
                if req in a:
                    print(vac)
                    flg = False
                    flag = False
            if flg == True:
                print('Вакансий не найдено\n')
            if flg == False:
                print("\nХотите вывести топ вакансий по зп в рублях? Если не хотите - 0. ")
                count = int(input('Введите кол-во: '))
                print()
                if count != 0:
                    result = b.get_top_vacancies_by_salary(count, answer_list_of_vacs)
                    for i in result:
                        print(i)

        except:
            print('Некорректный запрос!\n')

