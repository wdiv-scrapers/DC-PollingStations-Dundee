from geojson_scraper import scrape


stations_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_STATIONS&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_DISTRICTS&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'S12000042'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
