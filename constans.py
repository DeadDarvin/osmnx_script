BASE_QUERY = """
    [out:json];
    area["ISO3166-1"="KZ"][admin_level=2];
    nwr[place](area);
    out center;
    """

GET_LOCALITY_QUERY = """
    [out:json];
    area["ISO3166-1"="KZ"][admin_level=2]-> .a;
    (
    nwr(area.a)["place"="city"];
    nwr(area.a)["place"="town"];
    nwr(area.a)["place"="village"];
    nwr(area.a)["place"="hamlet"];    
    nwr(area.a)["place"="allotments"];    
    nwr(area.a)["place"="locality"];    
    );
    out center;
    """

BASE_URL = "https://maps.mail.ru/osm/tools/overpass/api/interpreter"
