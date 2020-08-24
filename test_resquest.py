import requests

BASE_URL = 'http://127.0.0.1:5000/'

# response = requests.get(BASE_URL + 'chemDB?db=chemDB&user=plant_chief&pword=plant123')
# print(response)

response = requests.post(BASE_URL + 'chemDB/insert?db=chemDB&user=plant_chief&pword=plant123')
print(response)
