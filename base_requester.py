import requests
from custom_logger import get_custom_loger

logger = get_custom_loger("new_test")

QUERY = """
    [out:json];
    area["ISO3166-1"="KZ"][admin_level=2];
    nwr[place](area);
    out center;
    """

class Requester:
    def __init__(self, url, query):
        self.url = url
        self.query = query

    def _get_raw_cities_list_from_request(self) -> list:
        response = requests.get(self.url, params={'data': self.query})
        data: dict = response.json()
        cities_list = data.get("elements")

        return cities_list

    def get_cities_coords_from_raw_list(self, raw_cities_list: list) -> list:
        """ """
        cities_coords: list = []
        for city in raw_cities_list:
            try:
                name = city["tags"]["name"]

                if city.get("center") is not None:
                    lat, lon = city["center"]["lat"], city["center"]["lon"]
                else:
                    lat, lon = city["lat"], city["lon"]

                cities_coords.append((name, lat, lon))

            except KeyError:
                logger.error(f" of getting name from: {city}", exc_info=True)

        return cities_coords


# def main():
#     raw_list = get_raw_cities_list_from_request("https://maps.mail.ru/osm/tools/overpass/api/interpreter", QUERY)
#     print(get_cities_coords_from_raw_list(raw_list))
#     print(len(raw_list))
#
#
# if __name__ == '__main__':
#     main()
