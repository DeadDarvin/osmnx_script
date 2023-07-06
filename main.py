from base_requester import Requester
from nominatim_requester import OSMRequester
from constans import BASE_URL, GET_LOCALITY_QUERY


def main():
    cities_list = Requester(BASE_URL, GET_LOCALITY_QUERY).get_cities_names_and_coords()
    osm_requester = OSMRequester(cities_list)
    osm_requester.search_request()


if __name__ == "__main__":
    main()