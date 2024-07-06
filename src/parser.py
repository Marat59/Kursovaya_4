from abc import ABC, abstractmethod

class Parser(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        """
        Загрузка вакансий по ключевому слову
        """
        pass

    @abstractmethod
    def get_top_vacancies_by_salary(self, count, listt):
        """
        Получение топ N вакансий по зарплате
        """
        pass

    @abstractmethod
    def get_vacancies_with_keyword_in_description(self, keyword):
        """
        Получение вакансий с ключевым словом в описании
        """
        pass
