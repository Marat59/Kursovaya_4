from conftest import vacHH, vac



def test_init_vac(vacHH):
    assert vacHH.get_url() == 'https://api.hh.ru/vacancies'
    assert vacHH.get_headers() == {'User-Agent': 'HH-User-Agent'}
    assert vacHH.get_params() == {'text': 'gyhuil', 'page': 0, 'per_page': 100}
    assert vacHH.get_vacs() == []
    assert vacHH.file_worker == None


def test_get_vacs(vacHH, vac):
    vacHH.set_vacs([vac])
    assert [vac] == vacHH.get_vacs()
