from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_STATIONS&outputFormat=json&srsName=EPSG%3A4326&sortBy=OBJECTID"
districts_url = "http://inspire.dundeecity.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3ASV_POLLING_DISTRICTS&outputFormat=json&srsName=EPSG%3A4326&sortBy=OBJECTID"
council_id = 'S12000042'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
