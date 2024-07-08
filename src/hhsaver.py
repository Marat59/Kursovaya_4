import json
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy
from pathlib import Path


class HHsaver(JSONSaver):
    """
    Класс для работы с вакансиями
    """

    def __init__(self):
        """
        Инициализация пустого листа для работы со словарями
        """
        self.__list_of_vacs = [] # мы хотим на выходе получить список словарей(переделанных вакансий, т.к. словарь = json файл

    @property
    def get_list(self):
        """
        Получение доступа к листу с вакансиями (с приватным атрибутом)
        """
        return self.__list_of_vacs

    @get_list.setter
    def get_list(self, change: Vacancy):
        """
        Дабавление вакансии в лист
        """
        if type(change) != Vacancy:
            raise ValueError
        self.__list_of_vacs.append(
                {'name': change.name,
                'link': change.link,
                'salary': change.salary,
                'description': change.get_description(),
                'cur': change.cur}
        )

    def vacancy_add(self, give_me_list): #на вход лист вакансий, или одну вакансию.
        """
        Добавление вакансии из файла JSON
        """
        if type(give_me_list) == list:  #тут на вход лист -> перебираем
            for vac in give_me_list:
                self.get_list = vac # Добавл каждый элемент листа
        if type(give_me_list) == Vacancy: # тут на вход экземляр Vacancy
            self.get_list = give_me_list # сразу его и добавляем
        with open(Path(__file__).parent.parent.joinpath('data').joinpath('vacancies.json'), 'w', encoding='utf-8') as file:
            json.dump(self.get_list, file, ensure_ascii=False, indent = 12)

    def vacancy_del(self, vac_name):
        """
        Удаление вакансии из файла JSON
        """
        with open(Path(__file__).parent.parent.joinpath('data').joinpath('vacancies.json'), 'r', encoding='utf-8') as file1:
            pythonvacs = json.load(file1)
            for py in pythonvacs:
                if vac_name == py.get('name'):
                    del pythonvacs[pythonvacs.index(py)]
        with open(Path(__file__).parent.parent.joinpath('data').joinpath('vacancies.json'), 'w', encoding='utf-8') as file2:
            json.dump(pythonvacs, file2, ensure_ascii=False, indent = 12)

    def vacancy_load(self):
        """
        Загрузка вакансий из файла JSON
        """
        with open(Path(__file__).parent.parent.joinpath('data').joinpath('vacancies.json'), 'r', encoding='utf-8') as file1:
            pythonvacs = json.load(file1)
            our_list = []
            for py in pythonvacs:
                obj = Vacancy(**py)
                our_list.append(obj)
            return our_list
