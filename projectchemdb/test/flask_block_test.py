""" Scirpt to easily formulate request to the local postgres data base """

import requests

BASE_URL = 'http://127.0.0.1:5000/'

creating = requests.get(BASE_URL + 'status')
print(creating.content)

searching = requests.get(BASE_URL + 'reactives' + "?view=*&where=chem_id&equals=CAC-068")
print((searching.content).decode())

inserting = requests.post(BASE_URL + 'reactive', json={
    "chem_id": "CAC-090",
    "name": "Sulfuric Acid",
    "chem_formula": "H2SO4",
    "cas_number": "7664-93-89",
    "nature": "INO",
    "ph_nature": "acid",
    "quantity": 28
})
print(inserting.content)

searching = requests.get(BASE_URL + 'reactives' + "?view=*&where=chem_id&equals=CAC-090")
print((searching.content).decode())

updating = requests.put(BASE_URL + 'reactive', json={
    "chem_id": "CAC-090",
    "chem_formula": "NaOH",
    "cas_number": "1310-73-55",
    "quantity": 15})

print(updating.content)

deleting = requests.delete(BASE_URL + 'reactive', json={"chem_id": "CAC-090"})
print(deleting.content)

