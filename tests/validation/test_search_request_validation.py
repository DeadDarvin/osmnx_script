from script.validation import check_objects_in_search_request
import pytest


@pytest.mark.parametrize(
    "city_name, lat, lon, json_response, expected_validation_result",
    [
        (
            "Аспара",
            "43.0431262",
            "73.5580482",
            [
                {
                    "place_id": 196229527,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 377729775,
                    "boundingbox": [
                        "43.3750385",
                        "43.382105",
                        "73.6088466",
                        "73.6157014"
                    ],
                    "lat": "43.37891",
                    "lon": "73.612267",
                    "display_name": "Аспара стансасы, Шу ауданы, Жамбыл облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.39999782720980437,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Аспара стансасы",
                        "county": "Шу ауданы",
                        "state": "Жамбыл облысы",
                        "ISO3166-2-lvl4": "KZ-31",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    73.6088466,
                                    43.3757227
                                ],
                                [
                                    73.6105113,
                                    43.3750385
                                ],
                                [
                                    73.6157014,
                                    43.3817281
                                ],
                                [
                                    73.6145728,
                                    43.382105
                                ],
                                [
                                    73.6140629,
                                    43.3816014
                                ],
                                [
                                    73.6128384,
                                    43.3816141
                                ],
                                [
                                    73.6116225,
                                    43.380344
                                ],
                                [
                                    73.6089163,
                                    43.3771196
                                ],
                                [
                                    73.6088466,
                                    43.3765843
                                ],
                                [
                                    73.6088466,
                                    43.3757227
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "Аспара стансасы",
                        "name:kk": "Аспара стансасы",
                        "name:ru": "станция Аспара",
                        "name:tt": "Аспара станциясе",
                        "name:uk": "станция Аспара",
                        "alt_name": "Аспара станциясы",
                        "int_name": "Aspara stansası",
                        "alt_name:kk": "Аспара станциясы",
                        "official_name": "Аспара"
                    }
                },
                {
                    "place_id": 22895797,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 2583605007,
                    "boundingbox": [
                        "43.0231262",
                        "43.0631262",
                        "73.5380482",
                        "73.5780482"
                    ],
                    "lat": "43.0431262",
                    "lon": "73.5580482",
                    "display_name": "Аспара, Меркі ауданы, Жамбыл облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.36000999999999994,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Аспара",
                        "county": "Меркі ауданы",
                        "state": "Жамбыл облысы",
                        "ISO3166-2-lvl4": "KZ-31",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            73.5580482,
                            43.0431262
                        ]
                    },
                    "namedetails": {
                        "name": "Аспара",
                        "name:kk": "Аспара",
                        "name:ru": "Аспара"
                    }
                },
                {
                    "place_id": 355528971,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 9527778725,
                    "boundingbox": [
                        "28.041718",
                        "28.081718",
                        "82.3369328",
                        "82.3769328"
                    ],
                    "lat": "28.061718",
                    "lon": "82.3569328",
                    "display_name": "अस्परा, घोराही-०९, घोराही, दाङ, नेपाल",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.25000999999999995,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "अस्परा",
                        "city_district": "घोराही-०९",
                        "municipality": "घोराही",
                        "county": "दाङ",
                        "country": "नेपाल",
                        "country_code": "np"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            82.3569328,
                            28.061718
                        ]
                    },
                    "namedetails": {
                        "name": "अस्परा",
                        "name:en": "Aspara",
                        "name:ne": "अस्परा"
                    }
                },
                {
                    "place_id": 3298418,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 457315723,
                    "boundingbox": [
                        "41.4322625",
                        "41.4722625",
                        "43.7602074",
                        "43.8002074"
                    ],
                    "lat": "41.4522625",
                    "lon": "43.7802074",
                    "display_name": "ასფარა, ნინოწმინდის მუნიციპალიტეტი, სამცხე-ჯავახეთი, საქართველო",
                    "class": "place",
                    "type": "village",
                    "importance": 0.1580839831692664,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "village": "ასფარა",
                        "county": "ნინოწმინდის მუნიციპალიტეტი",
                        "state": "სამცხე-ჯავახეთი",
                        "ISO3166-2-lvl4": "GE-SJ",
                        "country": "საქართველო",
                        "country_code": "ge"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            43.7802074,
                            41.4522625
                        ]
                    },
                    "namedetails": {
                        "name": "ასფარა",
                        "name:en": "Aspara",
                        "name:hy": "Ասփարա",
                        "name:ka": "ასფარა",
                        "name:ru": "Аспара"
                    }
                }
            ],
            True
        ),
        (
            "№98-темір жол айрығы",
            "42.9810504",
            "72.8114526",
            [
                {
                    "place_id": 196976745,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 377719947,
                    "boundingbox": [
                        "42.9787322",
                        "42.9833687",
                        "72.8086691",
                        "72.8142361"
                    ],
                    "lat": "42.981342",
                    "lon": "72.81208",
                    "display_name": "№98-темір жол айрығы, Тұрар Рысқұлов ауданы, Жамбыл облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.7346137428457797,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "№98-темір жол айрығы",
                        "county": "Тұрар Рысқұлов ауданы",
                        "state": "Жамбыл облысы",
                        "ISO3166-2-lvl4": "KZ-31",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    72.8086691,
                                    42.9793828
                                ],
                                [
                                    72.8092134,
                                    42.9787322
                                ],
                                [
                                    72.8096984,
                                    42.9789333
                                ],
                                [
                                    72.8099463,
                                    42.9796864
                                ],
                                [
                                    72.8124361,
                                    42.9802738
                                ],
                                [
                                    72.8139505,
                                    42.9816931
                                ],
                                [
                                    72.8142361,
                                    42.9828089
                                ],
                                [
                                    72.8129427,
                                    42.9833687
                                ],
                                [
                                    72.8110242,
                                    42.9815473
                                ],
                                [
                                    72.8093589,
                                    42.98081
                                ],
                                [
                                    72.8086691,
                                    42.9793828
                                ]
                            ]
                        ]
                    },
                    "namedetails": {
                        "name": "№98-темір жол айрығы",
                        "name:kk": "№98-темір жол айрығы",
                        "name:ru": "разъезд 98",
                        "name:tt": "№98-тимер юл разъезды",
                        "int_name": "№98-temir jol ayrığı"
                    }
                }
            ],
            True
        )
    ]
)
def test_search_request_validation_positive(city_name, lat, lon, json_response, expected_validation_result):
    assert check_objects_in_search_request(city_name, lat, lon, json_response) == expected_validation_result


@pytest.mark.parametrize(
    "city_name, lat, lon, json_response, expected_validation_result",
    [
        (
            "Жоламан",
            "44.261539",
            "77.548874",
            [
                {
                    "place_id": 56539952,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 5112398059,
                    "boundingbox": [
                        "52.9469284",
                        "52.9869284",
                        "76.0758791",
                        "76.1158791"
                    ],
                    "lat": "52.9669284",
                    "lon": "76.0958791",
                    "display_name": "Жоламан, Ақтоғай ауданы, Павлодар облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.40081240687427555,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Жоламан",
                        "county": "Ақтоғай ауданы",
                        "state": "Павлодар облысы",
                        "ISO3166-2-lvl4": "KZ-55",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            76.0958791,
                            52.9669284
                        ]
                    },
                    "namedetails": {
                        "name": "Жоламан",
                        "name:ru": "Жоламан"
                    }
                },
                {
                    "place_id": 3405692,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 474315845,
                    "boundingbox": [
                        "50.3420367",
                        "50.3820367",
                        "80.2513895",
                        "80.2913895"
                    ],
                    "lat": "50.3620367",
                    "lon": "80.2713895",
                    "display_name": "Жоламан, Семей, Абай облысы, 071000, Қазақстан",
                    "class": "place",
                    "type": "suburb",
                    "importance": 0.38500999999999996,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "suburb": "Жоламан",
                        "city": "Семей",
                        "state": "Абай облысы",
                        "ISO3166-2-lvl4": "KZ-10",
                        "postcode": "071000",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            80.2713895,
                            50.3620367
                        ]
                    },
                    "namedetails": {
                        "name": "Жоламан",
                        "name:ru": "Жоламан"
                    }
                }
            ],
            False
        )
    ]
)
def test_search_request_validation_bad_main_point(city_name, lat, lon, json_response, expected_validation_result):
    assert check_objects_in_search_request(city_name, lat, lon, json_response) == expected_validation_result


@pytest.mark.parametrize(
    "city_name, lat, lon, json_response, expected_validation_result",
    [
        (
            "Жоламан",
            "44.261539",
            "77.548874",
            [
                {
                    "place_id": 56539952,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 5112398059,
                    "boundingbox": [
                        "52.9469284",
                        "52.9869284",
                        "76.0758791",
                        "76.1158791"
                    ],
                    "lat": "44.261539",
                    "lon": "77.548874",
                    "display_name": "Жоламан, Ақтоғай ауданы, Павлодар облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.40081240687427555,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Жоламан",
                        "county": "Ақтоғай ауданы",
                        "state": "Павлодар облысы",
                        "ISO3166-2-lvl4": "KZ-55",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            76.0958791,
                            52.9669284
                        ]
                    },
                    "namedetails": {
                        "name": "Жоламан" + "invalid_text",
                        "name:ru": "Жоламан" + "invalid_text"
                    }
                }
            ],
            False
        )
    ]
)
def test_search_request_validation_bad_namedetails(city_name, lat, lon, json_response, expected_validation_result):
    assert check_objects_in_search_request(city_name, lat, lon, json_response) == expected_validation_result


@pytest.mark.parametrize(
    "city_name, lat, lon, json_response, expected_validation_result",
    [
        (
            "Жоламан",
            "44.261539",
            "77.548874",
            [
                {
                    "place_id": 56539952,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "node",
                    "osm_id": 5112398059,
                    "boundingbox": [
                        "52.9469284",
                        "52.9869284",
                        "76.0758791",
                        "76.1158791"
                    ],
                    "lat": "44.261539",
                    "lon": "77.548874",
                    "display_name": "Жоламан, Ақтоғай ауданы, Павлодар облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.40081240687427555,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Жоламан",
                        "county": "Ақтоғай ауданы",
                        "state": "Павлодар облысы",
                        "ISO3166-2-lvl4": "KZ-55",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            76.0958791,
                            52.9669284
                        ]
                    },
                    "namedetails": {
                        "name": "Жоламан",
                        "name:ru": "Жоламан"
                    }
                }
            ],
            False
        )
    ]
)
def test_search_request_validation_bad_osm_type(city_name, lat, lon, json_response, expected_validation_result):
    assert check_objects_in_search_request(city_name, lat, lon, json_response) == expected_validation_result


@pytest.mark.parametrize(
    "city_name, lat, lon, json_response, expected_validation_result",
    [
        (
            "Жоламан",
            "44.261539",
            "77.548874",
            [
                {
                    "place_id": 56539952,
                    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
                    "osm_type": "way",
                    "osm_id": 5112398059,
                    "boundingbox": [
                        "52.9469284",
                        "52.9869284",
                        "76.0758791",
                        "76.1158791"
                    ],
                    "lat": "44.261539",
                    "lon": "77.548874",
                    "display_name": "Жоламан, Ақтоғай ауданы, Павлодар облысы, Қазақстан",
                    "class": "place",
                    "type": "hamlet",
                    "importance": 0.40081240687427555,
                    "icon": "https://nominatim.openstreetmap.org/ui/mapicons/poi_place_village.p.20.png",
                    "address": {
                        "hamlet": "Жоламан",
                        "county": "Ақтоғай ауданы",
                        "state": "Павлодар облысы",
                        "ISO3166-2-lvl4": "KZ-55",
                        "country": "Қазақстан",
                        "country_code": "kz"
                    },
                    "geojson": {
                        "type": "Point",
                        "coordinates": [
                            76.0958791,
                            52.9669284
                        ]
                    },
                    "namedetails": {
                        "name": "Жоламан",
                        "name:ru": "Жоламан"
                    }
                }
            ],
            False
        )
    ]
)
def test_search_request_validation_without_polygon(city_name, lat, lon, json_response, expected_validation_result):
    assert check_objects_in_search_request(city_name, lat, lon, json_response) == expected_validation_result
