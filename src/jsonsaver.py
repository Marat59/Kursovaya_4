from abc import ABC, abstractmethod

class JSONSaver(ABC):
    """
    Класс сохраняющий вакансии в файл, загружающий вакансии из файла, удаляющий вакансию в файле
    """

    @abstractmethod
    def vacancy_add(self, vacancies):
        """
        Добавление вакансии в файл JSON
        """
        pass

    @abstractmethod
    def vacancy_load(self):
        """
        Загрузка вакансий из файла JSON
        """
        pass

    @abstractmethod
    def vacancy_del(self, vacancy):
        """
        Удаление вакансии из файла JSON
        """
        pass

