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
        self.__validate_salary()


    def __repr__(self):
        """
        Предоставление названия вакансии
        """
        return f'Вакансия: {self.name}'


    def __str__(self):
        """
        Предоставление названия вакансии и заработной платы
        """
        return f'{self.name}, {self.salary} {self.cur}, Описание вакансии: {self.get_description()}\n'


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

    def __validate_salary(self):
        """
        Валидация зарплаты
        """
        if not self.salary:
            self.salary = 0

    def validate(self):
        return self.__validate_salary()

    def get_description(self):
        """
        Получение доступа к описанию вакансии (с приватным атрибутом)
        """
        return self.__description
