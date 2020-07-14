import json
from codecs import open

with open('export.json', 'r', encoding='utf8') as f:
    data = f.read()
    osm_ddareungi_data = json.loads(data)
    print (len(osm_ddareungi_data['elements']), "elements in OSM data for seoul bike")