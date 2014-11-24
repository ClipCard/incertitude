incertitude is a simple project for quickly throwing together a geocoding service using public sources (GeoNames, in the example) and ElasticSearch.

### Use

Basic example loads data from GeoNames:

1. Download any of the city/place files from [GeoNames](http://download.geonames.org/export/dump/)

	```
	XX.zip
	allCountries.zip
	cities1000.zip
	cities5000.zip
	cities15000.zip
	```

2. Install and fire up [ElasticSearch](http://www.elasticsearch.org/overview/elkdownloads/). It should be running locally on port 9200.

3. Install the dependences with `pip install -r requirements.txt`
4. Run `incertitude.py`

	```bash
	python incertitude.py <mapping_file.json> <geonames_file_path>
	```
5. Give a whirl [in your browser](http://localhost:9200/geocode/place/_search?q=Greater Seattle Area)
	


### Customization

The mapping file is entirely customizable and is [standard ElasticSearch syntax](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-put-mapping.html). Simple tweaks can significantly change how queries are analyzed and the scoring of the results.

Further, the `incertitude.py` script is exceedingly simple - standard `csv` parsing and use of the `elasticsearch` library. This could be easily extended to extracting from an existing relational database with SQLAlchemy or other data stores.
