import requests
import time
headers = {
    "Authorization": "Bearer 0-GlZyKRIHcbz9fb9-5j"
}
response = requests.get(url="https://the-one-api.dev/v2/character", headers=headers)
print(response.status_code)
data = response.json()

list_of_names = {item['name']: item['gender'] for item in data['docs'][:10]}

print(list_of_names)


def get_info(name):
    for item in data['docs']:
        if item['name'].lower() == name.lower():
            print(item)


time.sleep(5)
response2 = requests.get(url="https://the-one-api.dev/v2/quote", headers=headers)
print(response2.status_code)
quote_data = response2.json()
print(quote_data['docs'][100])
