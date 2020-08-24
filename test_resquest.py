import requests


BASE_URL = 'http://127.0.0.1:5000/'

# response = requests.get(BASE_URL + 'chemDB?db=chemDB&user=plant_chief&pword=plant123')

response = requests.post(BASE_URL + 'chemDB/insert', json={
                        "chem_id":"MAN-001",
                        "name":"Hydrochloric Acid",
                        "chem_formula":"HCl",
                        "cas_number":"7647-01-0",
                        "nature":"INO",
                        "ph_nature":"acid",
                        "quantity":20}
                        )
