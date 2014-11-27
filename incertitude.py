
"""incertitude geonames loader is a working example of creating a simple
geocoder for possibly ambiguous input queries.

Usage:
  incertitude.py <mapping_file.json> <geonames_file_path> <settings_file.json>
  incertitude.py (-h | --help)
  incertitude.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import csv
import json
from docopt import docopt
from elasticsearch import Elasticsearch


if __name__ == '__main__':
    arguments = docopt(__doc__, version='incertitude geonames 1.0')
    db_path = arguments["<geonames_file_path>"]
    mapping_file = arguments["<mapping_file.json>"]
    settings_file = arguments["<settings_file.json>"]

    with file(mapping_file) as f:
        mapping = json.load(f)

    with file(settings_file) as f:
        settings = json.load(f)

    # by default we connect to localhost:9200
    es = Elasticsearch()

    body = {
        "settings": settings,
        "mappings": mapping
    }

    # create an index in elasticsearch, ignore status code 400 (index already exists)
    es.indices.delete(index='geocode', ignore=404)
    es.indices.create(index='geocode', ignore=400, body=body)
    with file(db_path) as db:
        reader = csv.reader(db, 'excel-tab')
        for row in reader:
            _id = row[0]
            name = row[1]
            country = row[8]
            lat = row[4]
            lng = row[5]
            population = row[14]

            data = {
                "name": name,
                "country": country,
                "population": population,
                "location": {
                    "lat": lat,
                    "lon": lng
                }
            }
            es.index(index="geocode", doc_type="place", id=_id, body=data)
