import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2021-10-30"

querystring = {"inboundpartialdate":"2019-12-01"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "b665dc1c0emsha3e12e786b85bc8p1c9c87jsna9c55d4a2f18"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
if(response.status_code == 429):
    print("Help me")