import requests
import pandas as pd
import json

#Function to fetch data from an API endpoint
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {endpoint}")
        return None

def load_data(data, path):
    id = data["id"]
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)

endpoint_users = "https://dummyjson.com/users/"
endpoint_products = "https://dummyjson.com/products/1"

#data_users = extract_data(endpoint_users)
#load_data(data_users, "users")

i = 1
while True:
    data_users = extract_data(endpoint_users + str(i))
    if data_users:
        load_data(data_users, "users")
    else: print(f"Error fetching data from {endpoint_users + str(i)}")
    i += 1