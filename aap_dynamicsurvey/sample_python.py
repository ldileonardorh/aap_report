# dynamic_inventory.py
import requests
import json

def fetch_inventory():
    # Replace with your actual API endpoint
    # response = requests.get('https://api.example.com/inventory')
    # data = response.json()

    inventory = {
        'all': {
            'hosts': 'localhost-localdomain'
        }
    }
    print(inventory)
    return inventory

if __name__ == '__main__':
    inventory = fetch_inventory()
    print(json.dumps(inventory))

