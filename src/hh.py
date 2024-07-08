import requests
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
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': 'gyhuil', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        self.file_worker = file_worker

    def get_url(self):
        """
        Получение URL
        """
        return self.__url

    def get_headers(self):
        """
        Получение заголовков
        """
        return self.__headers

    def get_params(self):
        """
        Получение параметров
        """
        return self.__params

    def get_vacs(self):
        """
        Получение листа с вакансиями
        """
        return self.__vacancies

    def set_vacs(self, input_vac):
        self.__vacancies = input_vac

    def load_vacancies(self, keyword):
        """
        Загрузка вакансий по ключевому слову
        """
        self.__params['text'] = keyword
        while self.get_params().get('page') != 20:
            response = requests.get(url=self.get_url(), params=self.get_params(), headers=self.get_headers())
            json_response = response.json() # json файл из ответа = словарь
            list_of_dict_vacs = json_response.get('items') #получаем значение из словаря по ключу items
            for one_vac in list_of_dict_vacs:
                if one_vac != None:
                    if one_vac.get('salary') != None:
                        self.__vacancies.append(Vacancy(
                            name=one_vac.get('name'),
                            link=one_vac.get('area').get('url'),
                            cur=one_vac.get('salary', {}).get('currency') or 0,
                            salary=one_vac.get('salary', {}).get('from') or 0,
                            description=one_vac.get('snippet', {}).get('requirement')
                        ))
            self.__params['page'] += 1

    def get_top_vacancies_by_salary(self, count, listt):
        """
        Получение топ N вакансий по зарплате
        на вход подать кол-во выводимых вакансий и готовый список экз класса Vacancy

        """
        array = []
        sorted_vacancies = sorted(listt, key=lambda vacancy: vacancy.salary,
                                  reverse=True)  # Сортируем по убыванию зарплаты
        for i in sorted_vacancies:
            if i.cur == 'RUR':
                array.append(i)
        return array[:count]

    def get_vacancies_with_keyword_in_description(self, keyword):
        """
        Получение вакансий с ключевым словом в описании
        """
        return [vacancy for vacancy in self.get_vacs() if keyword.lower() in vacancy.get_description().lower()]

