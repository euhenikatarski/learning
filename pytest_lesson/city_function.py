def get_city_country(city, country, population=''):

    if population:
        info = f'{city}, {country} - население {population}'
        return info.title()
    else:
        info = f'{city}, {country}'
        return info.title()

