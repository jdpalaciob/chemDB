import requests


BASE_URL = 'http://127.0.0.1:5000/'

response = requests.get(BASE_URL + 'chemDB')

# response = requests.post(BASE_URL + 'chemDB/insert', json={
#                         "chem_id":"CAC-001",
#                         "name":"Sulfuric Acid",
#                         "chem_formula":"H2SO4",
#                         "cas_number":"7664-93-9",
#                         "nature":"INO",
#                         "ph_nature":"acid",
#                         "quantity":28}
#                         )
# response = requests.post(BASE_URL + 'chemDB/insert', json={
#                         "chem_id":"MAN-002",
#                         "name":"Sodium Hydroxide",
#                         "nature":"INO",
#                         "ph_nature":"base",
#                         "quantity":25}
#                         )

response = requests.put(BASE_URL + 'chemDB/update', json={
                        "chem_id":"MAN-002",
                        "chem_formula":"NaOH",
                        "cas_number":"1310-73-2",
                        "quantity":15}
                        )