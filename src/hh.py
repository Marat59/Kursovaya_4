import requests
import json
from src.parser import Parser
from src.vacancy import Vacancy


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        """
        Инициализация парсера
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': 'gyhuil', 'page': 0, 'per_page': 100}
        self.vacancies = []
        self.file_worker = file_worker
        super().__init__(file_worker)

    def get_vacs(self):
        """
        Получение листа с вакансиями
        """
        return self.vacancies


    def load_vacancies(self, keyword):
        """
        Загрузка вакансий по ключевому слову
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, params=self.params, headers=self.headers, )
            jsonResponse = response.json() # json файл из ответа = словарь
            listOfDictVacs = jsonResponse.get('items') #получаем значение из словаря по ключу items
            for i in listOfDictVacs:
                if i != None:
                    if i.get('salary') != None:
                        self.vacancies.append(Vacancy(
                            name=i.get('name'),
                            link=i.get('area').get('url'),
                            cur=i.get('salary', {}).get('currency') or 0,
                            salary=i.get('salary', {}).get('from') or 0,
                            description=i.get('snippet', {}).get('requirement')
                        ))
            self.params['page'] += 1


    def get_top_vacancies_by_salary(self, count, listt):
        """
        Получение топ N вакансий по зарплате
        на вход подать кол-во выводимых вакансий и готовый список экз класса Vacancy

        """
        a = []
        sorted_vacancies = sorted(listt, key=lambda vacancy: vacancy.salary,
                                  reverse=True)  # Сортируем по убыванию зарплаты
        for i in sorted_vacancies:
            if i.cur == 'RUR':
                a.append(i)
        return a[:count]


    def get_vacancies_with_keyword_in_description(self, keyword):
        """
        Получение вакансий с ключевым словом в описании
        """
        return [vacancy for vacancy in self.vacancies if keyword.lower() in vacancy.get_description().lower()]

