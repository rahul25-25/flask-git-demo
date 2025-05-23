import requests

base_url = "http://127.0.0.1:8000"


user_data = {"name": "sagar", "age": 50}
user_data1 = {"name": "srujan", "age": 24}
ud1 ={"name": "raja", "age": 50}
ud2 ={"name": "tanvi", "age": 50}
ud3 ={"name": "anil", "age": 50}
ud4 ={"name": "sunil", "age": 50}
ud5 ={"name": "chintu", "age": 50}
ud6 ={"name": "binnu", "age": 50}

requests.post(f"{base_url}/users", json=user_data)
requests.post(f"{base_url}/users", json=ud1)
requests.post(f"{base_url}/users", json=ud2)
requests.post(f"{base_url}/users", json=ud3)
requests.post(f"{base_url}/users", json=ud4)
requests.post(f"{base_url}/users", json=ud5)
requests.post(f"{base_url}/users", json=ud6)



print("GET /users:", requests.get(f"{base_url}/users").json())