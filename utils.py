import re


def _get_city_tuple(string: str) -> tuple:
    string = re.sub("\n", "", string)
    params = string.split(" ::: ")
    coords = params[2].split(":")
    return params[1], coords[0], coords[1]


def get_cities_list_for_reverse_request(filename: str) -> list:
    """ Собирает города из файла в массив для запроса """
    cities_list_for_request = []
    with open(filename) as f_o:
        for line in f_o:
            city_info = _get_city_tuple(line)
            cities_list_for_request.append(city_info)

    return cities_list_for_request
