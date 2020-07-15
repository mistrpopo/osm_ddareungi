import json
from codecs import open
import pandas as pd

def load_osm_ddareungi_data():
    with open('export.json', 'r', encoding='utf8') as f:
        data = f.read()
        all_elements = json.loads(data)['elements']
        return pd.DataFrame(all_elements)

osm_ddareungi_data = load_osm_ddareungi_data()


def load_official_ddareungi_data():
    col_names=['district', 'id', 'name', 'address', 'latitude', 'longitude', 'open_since', 'capacity']
    official_ddareungi_data = pd.read_csv(r'ddareungi_official_data.csv', sep='\t', header=None, names=col_names)
    return official_ddareungi_data

official_ddareungi_data = load_official_ddareungi_data()

print (osm_ddareungi_data)
print (official_ddareungi_data))

# 133 rows vs 1540 rows
# TODO : 
# # flatten the "tags" json in OSM data to access it from pandas
# # compare data accuracy
# # search licence info at https://www.data.go.kr
# # follow the guidelines at https://wiki.openstreetmap.org/wiki/Import/Guidelines