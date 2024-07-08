from conftest import vac, vac2


def test_init_vac(vac):
    vac1 = vac
    assert vac1.name == "Менеджер голосовой поддержки в Яндекс"
    assert vac1.link == "https://api.hh.ru/areas/113"
    assert vac1.salary == 30000
    assert vac1.get_description() == "Способен работать в команде."
    assert vac1.cur == "RUR"


def test_repr_vas(vac):
    assert vac.__repr__() == 'Вакансия: Менеджер голосовой поддержки в Яндекс'


def test_str_vas(vac):
    assert vac.__str__() == 'Менеджер голосовой поддержки в Яндекс, 30000 RUR, Описание вакансии: Способен работать в команде.\n'

def test_lt_vas(vac, vac2):
    assert True == vac.__lt__(vac2)


def test_gt_vas(vac, vac2):
    assert False == vac.__gt__(vac2)


def test_validate_salary(vac):
    vac.salary = None
    vac.validate()
    assert vac.salary == 0


