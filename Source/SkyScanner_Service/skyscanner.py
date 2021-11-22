import requests

url = "https://tequila-api.kiwi.com/locations/query?term=PRG&locale=en-US&location_types=airport&active_only=true"


headers = {
    'apikey': "HYUX_bmghSqzT1oO3nRCcz7-Qtz9ng3U"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
if(response.status_code == 429):
    print("Help me")