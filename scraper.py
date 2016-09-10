from gml_scraper import scrape


stations_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_STATIONS&srsName=EPSG%3A4326"
stations_fields = {
    '{dundeecity.gov.uk/inspire}OBJECTID': 'OBJECTID',
    '{dundeecity.gov.uk/inspire}POLLING_DISTRICT': 'POLLING_DISTRICT',
    '{dundeecity.gov.uk/inspire}ID': 'ID',
    '{dundeecity.gov.uk/inspire}NAME': 'NAME',
    '{dundeecity.gov.uk/inspire}UPRN': 'UPRN',
    '{dundeecity.gov.uk/inspire}EASTING': 'EASTING',
    '{dundeecity.gov.uk/inspire}NORTHING': 'NORTHING',
    '{dundeecity.gov.uk/inspire}LATITUDE': 'LATITUDE',
    '{dundeecity.gov.uk/inspire}LONGITUDE': 'LONGITUDE',
}

districts_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_DISTRICTS&srsName=EPSG%3A4326"
districts_fields = {
    '{dundeecity.gov.uk/inspire}OBJECTID': 'OBJECTID',
    '{dundeecity.gov.uk/inspire}POLLING_DISTRICT': 'POLLING_DISTRICT',
    '{dundeecity.gov.uk/inspire}POLLING_STATION_UPRN': 'POLLING_STATION_UPRN',
    '{dundeecity.gov.uk/inspire}POLLING_STATION_NAME': 'POLLING_STATION_NAME',
    '{dundeecity.gov.uk/inspire}POLLING_STATION_ID': 'POLLING_STATION_ID',
}

council_id = 'S12000042'


scrape(stations_url, council_id, 'stations', stations_fields, 'OBJECTID', xml_format='wfs/2.0')
scrape(districts_url, council_id, 'districts', districts_fields, 'OBJECTID', xml_format='wfs/2.0')
