from city_function import get_city_country

def test_city_country():
    info = get_city_country('Homel', 'Belarus')
    assert info == 'Homel, Belarus'

def test_city_country_population():
    info = get_city_country('Homel', 'Belarus', '500000')
    assert info == 'Homel, Belarus - Население 500000'