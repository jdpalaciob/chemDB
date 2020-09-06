""" Scirpt to easily formulate request to the local postgres data base """

import requests

BASE_URL = 'http://127.0.0.1:5000/'

creating = requests.get(BASE_URL + 'status')

inserting = requests.post(BASE_URL + 'reactive', json={
    "chem_id": "CAC-001",
    "name": "Sulfuric Acid",
    "chem_formula": "H2SO4",
    "cas_number": "7664-93-9",
    "nature": "INO",
    "ph_nature": "acid",
    "quantity": 28
})

updating = requests.put(BASE_URL + 'reactive', json={
    "chem_id": "MAN-002",
    "chem_formula": "NaOH",
    "cas_number": "1310-73-2",
    "quantity": 15}
                        )

deleting = requests.delete(BASE_URL + 'reactive', json={
    "chem_id": "MAN-002"}
                           )

searching = requests.get(BASE_URL + 'reactives' + "?view=*&where=chem_id&equals=MAN-001")
print((searching.content).decode())
