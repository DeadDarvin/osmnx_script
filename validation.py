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


def check_object_in_search_request(real_name: str, data: list) -> bool:
    """ Общая проверка полученного резульатата """
    for _object in data:
        logger.debug(_object)

        display_name = _object.get("display_name")
        logger.debug(display_name)

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

        logger.debug("CHECK GEOJSON")
        geojson = _object.get("geojson")
        logger.debug(geojson)
        if geojson is None:
            logger.debug("WITHOUT GEOJSON")
            return False

        logger.debug("CHECK OBJECT HAS POLYGON")
        if not _object_has_polygon(geojson):
            logger.debug("WITHOUT POLYGON")
            return False

        logger.debug("OBJECT HAS POLYGON")

    return True
