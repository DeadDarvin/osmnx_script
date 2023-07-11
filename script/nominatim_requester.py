from .custom_logger import get_custom_loger
import requests
from .validation import check_objects_in_search_request, check_object_in_reverse_request
from requests.exceptions import JSONDecodeError, RequestException, ReadTimeout
from .utils import get_cities_list_for_reverse_request

logger = get_custom_loger(__name__)


class OSMRequester:

    def __init__(
            self,
            cities_list: list,
            search_filename: str,
            reverse_filename_with: str,
            reverse_filename_without: str
    ):
        self.cities_list = cities_list
        self.cities_list_length = len(cities_list)
        self.search_filename = search_filename
        self.reverse_filename_with_polygon = reverse_filename_with
        self.reverse_filename_without_polygon = reverse_filename_without

    @staticmethod
    def get_search_url(city: str):
        return "https://nominatim.openstreetmap.org/search?" \
               f"format=json&q={city}&" \
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
            if isinstance(data, dict):
                if data.get("error") is not None:
                    return

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
        with open(self.search_filename, "w") as f_o:
            for city in self.cities_list:
                name, lat, lon = city[0], city[1], city[2]
                search_url = self.get_search_url(name)

                data = self._get_city_object_from_request(search_url)
                if data is None:
                    gen_counter += 1
                    logger.error(f"BAD REQUEST {gen_counter}/{self.cities_list_length}")
                    continue

                logger.info(f"CHECK CITY: {name}")
                if not check_objects_in_search_request(name, lat, lon, data=data):
                    f_o.write(f"BAD:{counter} ::: {name} ::: {lat}:{lon}\n")
                    counter += 1
                    logger.warning(f"CITY {name} WITHOUT POLYGON {gen_counter}/{self.cities_list_length}")
                    gen_counter += 1
                    continue

                logger.info(f"CITY {name} WITH POLYGON {gen_counter}/{self.cities_list_length}")
                gen_counter += 1

    def reverse_request(self):
        cities_list = get_cities_list_for_reverse_request(self.search_filename)
        length = len(cities_list)

        counter = 1
        gen_counter = 1

        for city in cities_list:
            name, lat, lon = city[0], city[1], city[2]
            reverse_url = self.get_reverse_url(lat, lon)

            data = self._get_city_object_from_request(reverse_url)
            if data is None:
                logger.error(f"BAD REQUEST ::: {gen_counter}/{length}")
                gen_counter += 1
                continue

            logger.info(f"CHECK CITY: {name}")
            if not check_object_in_reverse_request(lat, lon, data=data):
                with open(self.reverse_filename_without_polygon, "a") as f_o:
                    f_o.write(f"BAD:{counter} ::: {name} ::: {lat}:{lon}\n")
                counter += 1
                logger.warning(f"CITY {name} WITHOUT POLYGON ::: {gen_counter}/{length}")
                gen_counter += 1
                continue

            with open(self.reverse_filename_with_polygon, "a") as f_o:
                f_o.write(f"GOOD:{counter} ::: {name} ::: {lat}:{lon}\n")

            logger.info(f"CITY {name} WITH POLYGON ::: {gen_counter}/{length}")
            gen_counter += 1
