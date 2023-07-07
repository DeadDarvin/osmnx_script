from custom_logger import get_custom_loger
import requests
from validation import check_object_in_search_request, check_object_in_reverse_request
from requests.exceptions import JSONDecodeError, RequestException, ReadTimeout

logger = get_custom_loger(__name__)


class OSMRequester:

    def __init__(self, cities_list: list):
        self.cities_list = cities_list
        self.cities_list_length = len(cities_list)

    @staticmethod
    def get_search_url(city: str):
        return "https://nominatim.openstreetmap.org/search?" \
               f"format=json&city={city}&" \
               "addressdetails=1&polygon_geojson=1&namedetails=1"

    @staticmethod
    def get_reverse_url(lat, lon):
        return "https://nominatim.openstreetmap.org/reverse?" \
               f"format=json&lat={lat}&lon={lon}&" \
               "zoom=15&addressdetails=1&polygon_geojson=1"

    @staticmethod
    def _get_city_object_from_request(request_url: str):

        try:
            response = requests.get(request_url, timeout=2)
            data = response.json()
            return data

        except JSONDecodeError:
            logger.error("IN JSONDecode", exc_info=True)
        except ReadTimeout:
            logger.error("TIMEOUT ERROR", exc_info=True)
        except ConnectionError:
            logger.error("IN REQUEST", exc_info=True)
        except RequestException:
            logger.error("UNKNOWN ERROR", exc_info=True)

    def search_request(self):
        gen_counter = 1
        counter = 1
        with open("test_search_requests2.txt", "w") as f_o:
            for city in self.cities_list:
                city_name = city[0]
                search_url = self.get_search_url(city_name)

                data = self._get_city_object_from_request(search_url)
                if data is None:
                    gen_counter += 1
                    logger.error(f"BAD REQUEST {gen_counter}/{self.cities_list_length}")
                    continue

                logger.info(f"CHECK CITY: {city_name}")
                if not check_object_in_search_request(real_name=city_name, data=data):
                    f_o.write(f"BAD:{counter} ::: {city_name} ::: {city[1]}:{city[2]}\n")
                    counter += 1
                    logger.warning(f"CITY {city_name} WITHOUT POLYGON {gen_counter}/{self.cities_list_length}")
                    gen_counter += 1
                    continue

                logger.info(f"CITY {city_name} WITH POLYGON {gen_counter}/{self.cities_list_length}")
                gen_counter += 1

    def reverse_request(self, cities_list):
        counter = 1
        gen_counter = 1
        length = len(cities_list)
        with open("test_reverse_request.txt", "w") as f_o:
            for city in cities_list:
                name, lat, lon = city[0], city[1], city[2]
                reverse_url = self.get_reverse_url(lat, lon)

                data = self._get_city_object_from_request(reverse_url)
                if data is None:
                    logger.error(f"BAD REQUEST ::: {gen_counter}/{length}")
                    gen_counter += 1
                    continue

                logger.info(f"CHECK CITY: {name}")
                if not check_object_in_reverse_request(name, lat, lon, data=data):
                    f_o.write(f"BAD:{counter} ::: {name} ::: {lat}:{lon}\n")
                    counter += 1
                    logger.warning(f"CITY {name} WITHOUT POLYGON ::: {gen_counter}/{length}")
                    gen_counter += 1
                    continue
                logger.info(f"CITY {name} WITH POLYGON ::: {gen_counter}/{length}")
                gen_counter += 1
