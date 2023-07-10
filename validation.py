from custom_logger import get_custom_loger
import re

logger = get_custom_loger("validation")
search_request_logger = get_custom_loger("search_validation")
reverse_request_logger = get_custom_loger("reverse_validation")
bad_main_point_logger = get_custom_loger("invalid_polygon")


def _object_has_polygon(geojson: dict) -> bool:
    """ Проверяет наличие полигона в объекте geojson """
    logger.debug("HAS POLYGON FUNC")
    _type = geojson.get("type")
    if _type != "Polygon" and _type != "MultiPolygon":
        return False

    return True


def _check_display_name_is_valid(real_name: str, display_name: str) -> bool:
    """ Проверка на вхождение overpass-city-name в display name из объекта"""
    logger.debug("CHECK DISPLAY_NAME FUNC")
    if re.search(real_name, display_name) is None:
        logger.debug(re.search(real_name, display_name))
        return False

    return True


def _check_country_code_is_valid(data: dict) -> bool:
    address = data.get("address")
    if address is None:
        logger.warning(f"CITY WITHOUT ADDRESS")
        return False

    country_code = address.get("country_code")

    if country_code is None or country_code != "kz":
        logger.debug("BAD COUNTRY CODE")
        return False

    return True


def _check_name_details_is_valid(real_name: str, namedetails: dict) -> bool:
    """ Проверяет совпадение реального имени с namedetails from json """
    logger.debug("CHECK_DETAILS_NAME FUNC")
    detail_names = namedetails.values()
    for detail_name in detail_names:
        logger.debug(real_name)
        logger.debug(detail_name)
        if str(real_name) == str(detail_name):
            return True

    return False


def _check_main_point_is_valid(real_lat, real_lon, data) -> bool:

    lat, lon = float(data.get("lat")), float(data.get("lon"))
    real_lat, real_lon = float(real_lat), float(real_lon)

    lat_difference = real_lat - lat
    lon_difference = real_lon - lon

    if abs(lat_difference) > 0.005 or abs(lon_difference) > 0.005:
        return False

    return True


def check_objects_in_search_request(real_name: str, lat: str, lon: str, data: list) -> bool:
    """
    Принимает список объектов.
    Если хотя бы один удовлетворяет требованиям,
    возвращает True. Иначе False.
    """
    for _object in data:
        search_request_logger.debug(_object)

        search_request_logger.info("CHECK MAIN_POINT_COORDS")
        if not _check_main_point_is_valid(lat, lon, _object):
            search_request_logger.error("BAD MAIN POINT")
            continue

        search_request_logger.debug("CHECK NAMEDETAILS")
        name_details = _object.get("namedetails")
        search_request_logger.debug(name_details)
        if name_details is None:
            continue

        if not _check_name_details_is_valid(real_name, name_details):
            search_request_logger.debug("BAD NAMEDETAILS")
            continue

        search_request_logger.debug("CHECK OSM TYPE")
        osm_type = _object.get("osm_type")
        if osm_type != "way" and osm_type != "relation":
            search_request_logger.debug("BAD OSM TYPE")
            continue

        geojson = _object.get("geojson")
        search_request_logger.debug(geojson)
        if geojson is None:
            search_request_logger.debug("WITHOUT GEOJSON")
            continue

        search_request_logger.debug("CHECK OBJECT HAS POLYGON")
        if not _object_has_polygon(geojson):
            search_request_logger.info("WITHOUT POLYGON")
            continue

        search_request_logger.debug("OBJECT HAS POLYGON")
        return True

    return False


def check_object_in_reverse_request(lat: str, lon: str, data: dict) -> bool:
    reverse_request_logger.debug(data)

    reverse_request_logger.debug("CHECK OSM TYPE")
    osm_type = data.get("osm_type")
    if osm_type != "way" and osm_type != "relation":
        reverse_request_logger.debug("BAD OSM TYPE")
        return False

    geojson = data.get("geojson")
    reverse_request_logger.debug(geojson)
    if geojson is None:
        reverse_request_logger.warning("WITHOUT GEOJSON")
        return False

    reverse_request_logger.debug("CHECK OBJECT HAS POLYGON")
    if _object_has_polygon(geojson):
        reverse_request_logger.info("CHECK MAIN_POINT_COORDS")
        if not _check_main_point_is_valid(lat, lon, data):
            reverse_request_logger.error(f"INVALID POLYGON IN: {data}")
            bad_main_point_logger.error(f"INVALID MAIN POINT IN {data}")
            return False
    else:
        logger.info("WITHOUT POLYGON")
        return False

    logger.debug("OBJECT HAS POLYGON")
    return True
