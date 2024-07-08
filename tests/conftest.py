import pytest
from src.hh import HH
from src.vacancy import Vacancy
from src.hhsaver import HHsaver


@pytest.fixture()
def vacHH():
    nameHH = HH(None)
    return nameHH


@pytest.fixture()
def vac():
    vac1 = Vacancy("Менеджер голосовой поддержки в Яндекс",
                   "https://api.hh.ru/areas/113",30000,
                   "Способен работать в команде.",
                   "RUR")
    return vac1


@pytest.fixture()
def vac2():
    vac2 = Vacancy("Менеджер по Wildberries / менеджер работе с marketplace",
                   "https://api.hh.ru/areas/1",100000,
                   "Опыт работы с marketplace (или желание развиваться в этой сфере).")
    return vac2



