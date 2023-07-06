from constans import GET_LOCALITY_QUERY, BASE_URL
from base_requester import Requester
from custom_logger import get_custom_loger
import requests

from validation import check_object_in_search_request

logger = get_custom_loger("test")

def get_search_url(city):
    return "https://nominatim.openstreetmap.org/search?" \
            f"format=json&city={city}&"\
           "addressdetails=1&polygon_geojson=1"

class OSMRequester:

    def __init__(self, cities_list):
        self.cities_list = cities_list
        self.cities_list_length = len(cities_list)


    @staticmethod
    def _get_city_object_from_request(request_url: str):

        try:
            response = requests.get(request_url)
            data = response.json()
            return data

        except ConnectionError:
            logger.error("IN SEARCH REQUEST", exc_info=True)

    @staticmethod
    def _get_city_object_from_reverse_request(lat, lon):
        """ Делает запрос на обратный геокодер """
        try:
            response = requests.get("https://nominatim.openstreetmap.org/reverse?"
                                    f"format=json&lat={lat}&lon={lon}&"
                                    "zoom=15&addressdetails=1&polygon_geojson=1")
            data = response.json()
            return data

        except ConnectionError:
            logger.error("IN REQUEST", exc_info=True)

    def search_request(self):
        with open("test_search_requests.txt", "w") as f_o:
            for i in range(30):
                search_url = get_search_url(self.cities_list[i][0])
                data = self._get_city_object_from_request(search_url)
                if not check_object_in_search_request(cities_list[i][0], data):
                    f_o.write(f"{i} ::: BAD ::: {cities_list[i][0]} ::: {str(data)}\n")
                    
                else:
                    f_o.write(f"{i} ::: GOOD ::: {cities_list[i][0]} ::: {str(data)}\n")

    def reverse_request(self):



def check_has_polygon_in_revers_request(city_info: tuple):
    """ Делает проверку на наличие полигона у объекта """
    data = get_city_object_from_reverse_request(city_info)
    if data is None:
        return

    try:
        geojson: dict = data["geojson"]

        if geojson.get("type") == "Polygon" :
            logger.info(f"OBJECT WITH COORDS - {city_info} - HAS POLYGON")
            return

        if geojson.get("type") == "LineString":
            logger.info(f"OBJECT WITH COORDS - {city_info} - HAS LINESTRING")
            return

        with open("without_polygones.txt", "a") as f_o:
            f_o.write(f'{data["place_id"]} ::: {data["display_name"]} ::: {data["lat"]}:{data["lon"]}\n')

    except KeyError:
        logger.error("IN CITY_OBJECT", exc_info=True)


if __name__ == "__main__":
    cities_list = Requester(BASE_URL, GET_LOCALITY_QUERY).get_cities_names_and_coords()
    osm_requester = OSMRequester(cities_list)
    osm_requester.search_request()
