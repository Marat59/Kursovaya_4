import pytest
from src.hh import HH
from tests.test_vacancy import vac


@pytest.fixture()
def vacHH():
    nameHH = HH(None)
    return nameHH

def test_init_vac(vacHH):
    vac1 = vacHH
    assert vac1.url == 'https://api.hh.ru/vacancies'
    assert vac1.headers == {'User-Agent': 'HH-User-Agent'}
    assert vac1.params == {'text': 'gyhuil', 'page': 0, 'per_page': 100}
    assert vac1.vacancies == []
    assert vac1.file_worker == None


def test_get_vacs(vacHH, vac):
    vacHH.vacancies = [vac]
    assert [vac] == vacHH.get_vacs()
