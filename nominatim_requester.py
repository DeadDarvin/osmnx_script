from custom_logger import get_custom_loger
import requests
from validation import check_object_in_search_request

logger = get_custom_loger(__name__)


class OSMRequester:

    def __init__(self, cities_list):
        self.cities_list = cities_list
        self.cities_list_length = len(cities_list)

    @staticmethod
    def get_search_url(city: str):
        return "https://nominatim.openstreetmap.org/search?" \
               f"format=json&city={city}&" \
               "addressdetails=1&polygon_geojson=1"

    @staticmethod
    def get_reverse_url(lat, lon):
        return "https://nominatim.openstreetmap.org/reverse?" \
               f"format=json&lat={lat}&lon={lon}&" \
               "zoom=15&addressdetails=1&polygon_geojson=1"

    @staticmethod
    def _get_city_object_from_request(request_url: str):

        try:
            response = requests.get(request_url)
            data = response.json()
            return data

        except ConnectionError:
            logger.error("IN REQUEST", exc_info=True)

    def search_request(self):
        counter = 1
        with open("test_search_requests.txt", "w") as f_o:
            for city in self.cities_list:
                city_name = city[0]
                search_url = self.get_search_url(city_name)

                data = self._get_city_object_from_request(search_url)
                if data is None:
                    continue
                logger.info(f"CHECK CITY: {city_name}")
                if not check_object_in_search_request(real_name=city_name, data=data):
                    f_o.write(f"BAD:{counter} ::: {city_name} ::: {city[1]}:{city[2]}\n")
                    counter += 1
