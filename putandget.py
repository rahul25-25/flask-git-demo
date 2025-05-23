import requests

base_url = "http://127.0.0.1:8000"

get_value = requests.get(f"{base_url}/users").json()
print(get_value)
data_u ={"name": "tanvi", "age": 5}
requests.put(f"{base_url}/users/5", json=data_u)
get_value1 = requests.get(f"{base_url}/users/5").json()
print(get_value1)
get_value = requests.get(f"{base_url}/users").json()
print(get_value)
