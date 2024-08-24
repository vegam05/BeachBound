import requests

def returner(lat,lon,model,parameters,level,key):
    url = "https://api.windy.com/api/point-forecast/v2"
    payload = {
    "lat": lat,
    "lon": lon,
    "model": model,
    "parameters": parameters,
    "levels": level,
    "key": key
}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return "Error:", response.status_code, response.text