from validation import _check_main_point_is_valid
import pytest


@pytest.mark.parametrize(
    "real_lat, real_lon, data, expected_result",
    [
        (
            "41.3719735",
            "68.9994411",
            {
                    "place_id": 143201235,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 150880273,
                    "boundingbox": [
                        "41.3600612",
                        "41.3838858",
                        "68.9785612",
                        "69.0203211"
                    ],
                    "lat": "41.371849",
                    "lon": "69.00418",
                    "display_name": "Ораз ата ауылы, Келес ауданы, Түркістан облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.6577843968154352,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Ораз ата ауылы",
                        "county": "Келес ауданы",
                        "state": "Түркістан облысы",
                        "ISO3166-2-lvl4": "KZ-61",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    68.9785612,
                                    41.3693828
                                ],
                                [
                                    68.9809375,
                                    41.3671714
                                ],
                                [
                                    68.9861021,
                                    41.3672903
                                ],
                                [
                                    68.9944242,
                                    41.3693809
                                ],
                                [
                                    68.9964815,
                                    41.3680529
                                ],
                                [
                                    68.9938629,
                                    41.3666291
                                ],
                                [
                                    68.9928211,
                                    41.3652335
                                ],
                                [
                                    68.993314,
                                    41.3644601
                                ],
                                [
                                    69.0028631,
                                    41.3600612
                                ],
                                [
                                    69.0100554,
                                    41.3607746
                                ],
                                [
                                    69.0157586,
                                    41.3619161
                                ],
                                [
                                    69.015917,
                                    41.365602
                                ],
                                [
                                    69.0118297,
                                    41.3697395
                                ],
                                [
                                    69.0203211,
                                    41.3718319
                                ],
                                [
                                    69.0202847,
                                    41.3752973
                                ],
                                [
                                    69.0127486,
                                    41.3798205
                                ],
                                [
                                    68.9983322,
                                    41.3838858
                                ],
                                [
                                    68.9887002,
                                    41.3825783
                                ],
                                [
                                    68.986514,
                                    41.3810092
                                ],
                                [
                                    68.9903478,
                                    41.3740907
                                ],
                                [
                                    68.9801771,
                                    41.3721172
                                ],
                                [
                                    68.9785612,
                                    41.3693828
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "Ораз ата ауылы",
                        "name:en": "Oraz ata",
                        "name:kk": "Ораз ата ауылы",
                        "name:ru": "Ораз Ата",
                        "name:tg": "Ораз ота",
                        "name:uk": "Ораз-ата",
                        "int_name": "Oraz ata awılı",
                        "old_name": "Димитров",
                        "old_name:kk": "Димитров",
                        "old_name:ru": "Димитрово"
                    }
                },
            True
        ),
        (
            "41.3719735",
            "68.9994411",
            {
                    "place_id": 143201235,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 150880273,
                    "boundingbox": [
                        "41.3600612",
                        "41.3838858",
                        "68.9785612",
                        "69.0203211"
                    ],
                    "lat": "41.3719746793",
                    "lon": "69.00418",
                    "display_name": "Ораз ата ауылы, Келес ауданы, Түркістан облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.6577843968154352,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Ораз ата ауылы",
                        "county": "Келес ауданы",
                        "state": "Түркістан облысы",
                        "ISO3166-2-lvl4": "KZ-61",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    68.9785612,
                                    41.3693828
                                ],
                                [
                                    68.9809375,
                                    41.3671714
                                ],
                                [
                                    68.9861021,
                                    41.3672903
                                ],
                                [
                                    68.9944242,
                                    41.3693809
                                ],
                                [
                                    68.9964815,
                                    41.3680529
                                ],
                                [
                                    68.9938629,
                                    41.3666291
                                ],
                                [
                                    68.9928211,
                                    41.3652335
                                ],
                                [
                                    68.993314,
                                    41.3644601
                                ],
                                [
                                    69.0028631,
                                    41.3600612
                                ],
                                [
                                    69.0100554,
                                    41.3607746
                                ],
                                [
                                    69.0157586,
                                    41.3619161
                                ],
                                [
                                    69.015917,
                                    41.365602
                                ],
                                [
                                    69.0118297,
                                    41.3697395
                                ],
                                [
                                    69.0203211,
                                    41.3718319
                                ],
                                [
                                    69.0202847,
                                    41.3752973
                                ],
                                [
                                    69.0127486,
                                    41.3798205
                                ],
                                [
                                    68.9983322,
                                    41.3838858
                                ],
                                [
                                    68.9887002,
                                    41.3825783
                                ],
                                [
                                    68.986514,
                                    41.3810092
                                ],
                                [
                                    68.9903478,
                                    41.3740907
                                ],
                                [
                                    68.9801771,
                                    41.3721172
                                ],
                                [
                                    68.9785612,
                                    41.3693828
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "Ораз ата ауылы",
                        "name:en": "Oraz ata",
                        "name:kk": "Ораз ата ауылы",
                        "name:ru": "Ораз Ата",
                        "name:tg": "Ораз ота",
                        "name:uk": "Ораз-ата",
                        "int_name": "Oraz ata awılı",
                        "old_name": "Димитров",
                        "old_name:kk": "Димитров",
                        "old_name:ru": "Димитрово"
                    }
                },
            True
        )
    ]
)
def test_check_main_point_is_valid_positive(real_lat, real_lon, data, expected_result):
    assert _check_main_point_is_valid(real_lat, real_lon, data) == expected_result


@pytest.mark.parametrize(
    "real_lat, real_lon, data, expected_result",
    [
        (
            "41.3719735",
            "68.9994411",
            {
                    "place_id": 143201235,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 150880273,
                    "boundingbox": [
                        "41.3600612",
                        "41.3838858",
                        "68.9785612",
                        "69.0203211"
                    ],
                    "lat": "41.371849",
                    "lon": "70.00418",  # ERROR
                    "display_name": "Ораз ата ауылы, Келес ауданы, Түркістан облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.6577843968154352,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Ораз ата ауылы",
                        "county": "Келес ауданы",
                        "state": "Түркістан облысы",
                        "ISO3166-2-lvl4": "KZ-61",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    68.9785612,
                                    41.3693828
                                ],
                                [
                                    68.9809375,
                                    41.3671714
                                ],
                                [
                                    68.9861021,
                                    41.3672903
                                ],
                                [
                                    68.9944242,
                                    41.3693809
                                ],
                                [
                                    68.9964815,
                                    41.3680529
                                ],
                                [
                                    68.9938629,
                                    41.3666291
                                ],
                                [
                                    68.9928211,
                                    41.3652335
                                ],
                                [
                                    68.993314,
                                    41.3644601
                                ],
                                [
                                    69.0028631,
                                    41.3600612
                                ],
                                [
                                    69.0100554,
                                    41.3607746
                                ],
                                [
                                    69.0157586,
                                    41.3619161
                                ],
                                [
                                    69.015917,
                                    41.365602
                                ],
                                [
                                    69.0118297,
                                    41.3697395
                                ],
                                [
                                    69.0203211,
                                    41.3718319
                                ],
                                [
                                    69.0202847,
                                    41.3752973
                                ],
                                [
                                    69.0127486,
                                    41.3798205
                                ],
                                [
                                    68.9983322,
                                    41.3838858
                                ],
                                [
                                    68.9887002,
                                    41.3825783
                                ],
                                [
                                    68.986514,
                                    41.3810092
                                ],
                                [
                                    68.9903478,
                                    41.3740907
                                ],
                                [
                                    68.9801771,
                                    41.3721172
                                ],
                                [
                                    68.9785612,
                                    41.3693828
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "Ораз ата ауылы",
                        "name:en": "Oraz ata",
                        "name:kk": "Ораз ата ауылы",
                        "name:ru": "Ораз Ата",
                        "name:tg": "Ораз ота",
                        "name:uk": "Ораз-ата",
                        "int_name": "Oraz ata awılı",
                        "old_name": "Димитров",
                        "old_name:kk": "Димитров",
                        "old_name:ru": "Димитрово"
                    }
                },
            False
        )
    ]
)
def test_check_main_point_is_valid_bad_lon(real_lat, real_lon, data, expected_result):
    assert _check_main_point_is_valid(real_lat, real_lon, data) == expected_result


@pytest.mark.parametrize(
    "real_lat, real_lon, data, expected_result",
    [
        (
            "41.3719735",
            "68.9994411",
            {
                    "place_id": 143201235,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 150880273,
                    "boundingbox": [
                        "41.3600612",
                        "41.3838858",
                        "68.9785612",
                        "69.0203211"
                    ],
                    "lat": "40.371849",
                    "lon": "69.00418",
                    "display_name": "Ораз ата ауылы, Келес ауданы, Түркістан облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.6577843968154352,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Ораз ата ауылы",
                        "county": "Келес ауданы",
                        "state": "Түркістан облысы",
                        "ISO3166-2-lvl4": "KZ-61",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    68.9785612,
                                    41.3693828
                                ],
                                [
                                    68.9809375,
                                    41.3671714
                                ],
                                [
                                    68.9861021,
                                    41.3672903
                                ],
                                [
                                    68.9944242,
                                    41.3693809
                                ],
                                [
                                    68.9964815,
                                    41.3680529
                                ],
                                [
                                    68.9938629,
                                    41.3666291
                                ],
                                [
                                    68.9928211,
                                    41.3652335
                                ],
                                [
                                    68.993314,
                                    41.3644601
                                ],
                                [
                                    69.0028631,
                                    41.3600612
                                ],
                                [
                                    69.0100554,
                                    41.3607746
                                ],
                                [
                                    69.0157586,
                                    41.3619161
                                ],
                                [
                                    69.015917,
                                    41.365602
                                ],
                                [
                                    69.0118297,
                                    41.3697395
                                ],
                                [
                                    69.0203211,
                                    41.3718319
                                ],
                                [
                                    69.0202847,
                                    41.3752973
                                ],
                                [
                                    69.0127486,
                                    41.3798205
                                ],
                                [
                                    68.9983322,
                                    41.3838858
                                ],
                                [
                                    68.9887002,
                                    41.3825783
                                ],
                                [
                                    68.986514,
                                    41.3810092
                                ],
                                [
                                    68.9903478,
                                    41.3740907
                                ],
                                [
                                    68.9801771,
                                    41.3721172
                                ],
                                [
                                    68.9785612,
                                    41.3693828
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "Ораз ата ауылы",
                        "name:en": "Oraz ata",
                        "name:kk": "Ораз ата ауылы",
                        "name:ru": "Ораз Ата",
                        "name:tg": "Ораз ота",
                        "name:uk": "Ораз-ата",
                        "int_name": "Oraz ata awılı",
                        "old_name": "Димитров",
                        "old_name:kk": "Димитров",
                        "old_name:ru": "Димитрово"
                    }
                },
            False
        )
    ]
)
def test_check_main_point_is_valid_bad_lat(real_lat, real_lon, data, expected_result):
    assert _check_main_point_is_valid(real_lat, real_lon, data) == expected_result
