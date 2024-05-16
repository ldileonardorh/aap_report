import requests
import json

def get_subscription_names(access_token):
    # Define the necessary URL
    subscription_url = 'https://management.azure.com/subscriptions?api-version=2021-01-01'

    # List Subscriptions
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    subscription_response = requests.get(subscription_url, headers=headers)
    subscription_response.raise_for_status()
    subscriptions = subscription_response.json()

    # Extract subscription names
    subscription_names = [subscription['displayName'] for subscription in subscriptions['value']]

    # Return the list of subscription names as a JSON array
    return json.dumps(subscription_names)

# Define your access token
access_token = 'your-access-token'

# Get the JSON array of subscription names
subscription_names_json = get_subscription_names(access_token)
print(subscription_names_json)

