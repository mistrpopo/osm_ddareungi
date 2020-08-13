import json
from codecs import open
import pandas as pd

def load_osm_ddareungi_data():
    with open('export.json', 'r', encoding='utf8') as f:
        data = f.read()
        all_elements = json.loads(data)['elements']
        for element in all_elements:
            if 'tags' in element:
                # flatten the data
                tags = element['tags']
                for key, value in tags.items():
                    element[key] = value
                del element['tags']
        return pd.DataFrame(all_elements)

osm_ddareungi_data = load_osm_ddareungi_data()


def load_official_ddareungi_data():
    col_names=['district', 'id', 'name', 'address', 'latitude', 'longitude', 'open_since', 'capacity']
    official_ddareungi_data = pd.read_csv(r'ddareungi_official_data.csv', sep='\t', header=None, names=col_names)
    return official_ddareungi_data

official_ddareungi_data = load_official_ddareungi_data()

print ('\n\n\n\n')
print ("================================================")
print ("============OPENSTREETMAP DATA==================")
print ("================================================")
print (osm_ddareungi_data, '\n\n')
print ("=====================================================")
print ("============OFFICIAL DDAREUNGI DATA==================")
print ("=====================================================")
print (official_ddareungi_data)


# list all districts
# print (official_ddareungi_data.district.unique())
allDistricts = [
    '마포구', '서대문구', '영등포구', '광진구', '성동구', '중구', '종로구', 
    '동대문구', '양천구', '용산구', '은평구', '강동구', '강서구', '송파구', 
    '중랑구', '성북구', '노원구', '도봉구', '금천구', '강북구', '구로구', 
    '동작구', '관악구', '서초구', '강남구']


# 133 rows vs 1540 rows
# TODO : 
# # compare data accuracy
# # search licence info at https://www.data.go.kr
# # follow the guidelines at https://wiki.openstreetmap.org/wiki/Import/Guidelines