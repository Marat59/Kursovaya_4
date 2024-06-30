
class Vacancy:
    """
    Класс для работы с вакансией
    """
    def __init__(self, name, link, salary=0, description='', cur = 'RUR'):
        """
        Инициализация вакансии
        """
        self.name = name
        self.link = link
        self.salary = salary
        self.__description = description
        self.cur = cur


    def __repr__(self):
        """
        Предоставление названия вакансии
        """
        return f'Вакансия: {self.name}'


    def __str__(self):
        """
        Предоставление названия вакансии и заработной платы
        """
        return f'{self.name}, {self.salary} {self.cur}'


    def __lt__(self, other):
        """
        Сравнение вакансий по зарплате
        """
        return self.salary < other.salary


    def __gt__(self, other):
        """
        Сравнение вакансий по зарплате
        """
        return self.salary > other.salary
    def validate_salary(self):
        """
        Валидация зарплаты
        """
        if not self.salary:
            self.salary = 0

    def get_description(self):
        """
        Получение доступа к описанию вакансии (с приватным атрибутом)
        """
        return self.__description
