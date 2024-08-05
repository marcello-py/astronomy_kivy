import requests

url = "https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)
j_son = response.json()
print(j_son)
