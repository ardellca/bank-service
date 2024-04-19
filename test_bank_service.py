import requests


def test_get_all_banks(url: str):
    res = requests.get(url).json()
    assert (res == [{'banks_id': 1,
                     'name': 'Альфа-Банк',
                     'description': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
                     'count_clients': 10000,
                     'age': 34},
                    {'banks_id': 2,
                     'name': 'ВТБ',
                     'description': 'Крупнейший российский банк, предоставляющий полный спектр финансовых услуг для корпоративных и частных клиентов',
                     'count_clients': 15000,
                     'age': 30},
                    {'banks_id': 3,
                     'name': 'Ozon',
                     'description': 'Ведущая мультикатегорийная платформа электронной коммерции и одна из крупнейших интернет-компаний в России',
                     'count_clients': 'MarketPlace',
                     'age': 26},
                    {'banks_id': 4,
                     'name': 'Apple',
                     'description': 'Американская корпорация, разработчик персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения и цифрового контента',
                     'count_clients': 'Electronic Device',
                     'age': 47}])


def test_get_bank_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'banks_id': 1,
                    'name': 'Альфа-Банк',
                    'description': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
                    'count_clients': 10000,
                    'age': 34})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/banks/'
    test_get_bank_by_id(URL + '1')
    test_get_all_banks(URL)
