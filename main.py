from base_requester import Requester
from nominatim_requester import OSMRequester
from constans import BASE_URL, GET_LOCALITY_QUERY
from utils import get_cities_list_for_reverse_request


def main():
    cities_list = Requester(BASE_URL, GET_LOCALITY_QUERY).get_cities_names_and_coords()
    osm_requester = OSMRequester(cities_list)
    osm_requester.search_request()
    lst = get_cities_list_for_reverse_request("test_search_requests2.txt")
    osm_requester.reverse_request(lst)


def test():
    lst = get_cities_list_for_reverse_request("test_search_requests.txt")
    osm_requester = OSMRequester(lst)
    osm_requester.reverse_request(lst)


if __name__ == "__main__":
    main()
