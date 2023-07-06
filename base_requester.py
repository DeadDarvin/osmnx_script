import requests
from custom_logger import get_custom_loger


logger = get_custom_loger(__name__)


class Requester:

    def __init__(self, url, query):
        self.url = url
        self.query = query

    def _get_raw_cities_list_from_request(self) -> list:
        try:
            response = requests.get(self.url, params={'data': self.query})

            data: dict = response.json()
            cities_list = data.get("elements")

            return cities_list

        except ConnectionError:
            logger.error("IN REQUEST", exc_info=True)

    def get_cities_names_and_coords(self) -> list:
        """ """
        raw_cities_list = self._get_raw_cities_list_from_request()
        cities_names_and_coords = []

        for city in raw_cities_list:
            try:
                name = city["tags"]["name"]

                if city.get("center") is not None:
                    lat, lon = city["center"]["lat"], city["center"]["lon"]
                else:
                    lat, lon = city["lat"], city["lon"]

                cities_names_and_coords.append((name, lat, lon))

            except KeyError:
                logger.error(f" of getting name from: {city}", exc_info=True)

        return cities_names_and_coords
