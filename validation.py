from custom_logger import get_custom_loger
import re

logger = get_custom_loger("validation")


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

    if int(lat) != int(float(real_lat)):
        return False
    if int(lon) != int(float(real_lon)):
        return False

    return True


def check_object_in_search_request(real_name: str, data: list) -> bool:
    """ Общая проверка полученного резульатата """
    for _object in data:
        logger.debug(_object)

        logger.debug("CHECK NAMEDETAILS")
        name_details = _object.get("namedetails")
        logger.debug(name_details)
        if name_details is not None:
            if not _check_name_details_is_valid(real_name, name_details):
                logger.debug("BAD NAMEDETAILS")
                continue
        else:
            display_name = _object.get("display_name")

            if display_name is None:
                logger.debug("HAS NOT DISPLAY NAME")
                continue

            if not _check_display_name_is_valid(real_name, str(display_name)):
                logger.debug("BAD DISPLAY NAME")
                continue

        logger.debug("CHECK OSM TYPE")
        osm_type = _object.get("osm_type")
        logger.debug(osm_type)
        if osm_type != "way" and osm_type != "relation":
            logger.debug("BAD OSM TYPE")
            continue

        logger.debug("CHECK COUNTRY_CODE")
        if not _check_country_code_is_valid(_object):
            continue

        logger.debug("CHECK GEOJSON")
        geojson = _object.get("geojson")
        logger.debug(geojson)
        if geojson is None:
            logger.debug("WITHOUT GEOJSON")
            continue

        logger.debug("CHECK OBJECT HAS POLYGON")
        if not _object_has_polygon(geojson):
            logger.info("WITHOUT POLYGON")
            continue

        logger.debug("OBJECT HAS POLYGON")
        return True

    return False


def check_object_in_reverse_request(name:str, lat: str, lon: str, data: dict) -> bool:
    logger.debug(data)

    logger.debug("CHECK OSM TYPE")
    osm_type = data.get("osm_type")
    logger.debug(osm_type)
    if osm_type != "way" and osm_type != "relation":
        logger.debug("BAD OSM TYPE")
        return False

    logger.debug("CHECK GEOJSON")
    geojson = data.get("geojson")
    logger.debug(geojson)
    if geojson is None:
        logger.debug("WITHOUT GEOJSON")
        return False

    logger.info("CHECK OBJECT HAS POLYGON")
    if _object_has_polygon(geojson):
        logger.info("CHECK MAIN_POINT_COORDS")
        if not _check_main_point_is_valid(lat, lon, data):
            logger.error("INVALID POLYGON IN: ", data)
            return False
    else:
        logger.info("WITHOUT POLYGON")
        return False

    logger.debug("OBJECT HAS POLYGON")
    return True
