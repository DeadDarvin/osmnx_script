from base_requester import Requester
from nominatim_requester import OSMRequester
from constans import BASE_URL, GET_LOCALITY_QUERY
from utils import get_cities_list_for_reverse_request


def main():
    cities_list = Requester(BASE_URL, GET_LOCALITY_QUERY).get_cities_names_and_coords()
    osm_requester = OSMRequester(
        cities_list,
        search_filename="home_search_request.txt",
        reverse_filename="home_reverse_request.txt"
    )
    osm_requester.search_request()
    osm_requester.reverse_request()


if __name__ == "__main__":
    main()
