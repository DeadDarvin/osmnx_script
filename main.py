from script.base_requester import Requester
from script.nominatim_requester import OSMRequester
from script.constans import BASE_URL, GET_LOCALITY_QUERY


def main():
    cities_list = Requester(BASE_URL, GET_LOCALITY_QUERY).get_cities_names_and_coords()
    osm_requester = OSMRequester(
        cities_list,
        search_filename="server_search_request.txt",
        reverse_filename="server_reverse_request.txt"
    )
    osm_requester.search_request()
    osm_requester.reverse_request()


# def main2():
#     osm_requester = OSMRequester([("Ораз ата ауылы", "41.3719735", "68.9994411"), ], "test.txt", "test2.txt")
#     osm_requester.search_request()
#     # print(osm_requester._get_city_object_from_request("https://nominatim.openstreetmap.org/search?"
#     #                                             f"format=json&q=Ораз ата ауылы&"
#     #                                             "addressdetails=1&polygon_geojson=1&namedetails=1"))


if __name__ == "__main__":
    main()
