from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper

root_url="https://dservices.arcgis.com/GlZ1P6ksdiXNYhvC/arcgis/services/Dundee_Polling_Districts_and_Polling_Stations/WFSServer"
stations_url = "{root_url}?outputFormat=GEOJSON&request=GetFeature&service=wfs&typename=Polling_Stations".format(root_url=root_url)
districts_url = "{root_url}?outputFormat=GEOJSON&request=GetFeature&service=wfs&typename=Polling_Districts".format(root_url=root_url)
council_id = 'DND'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
