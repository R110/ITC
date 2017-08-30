import itertools
import requests
import json
import base64
import inspect

def send_request(method, params):
    url = "http://hack.israeltechallenge.com:8000/"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    }
    return requests.post(url, data=json.dumps(payload), headers=headers).json()

response = send_request('help', [])
print(response)
print('-----------------------')
# response = send_request('verify_access_token', [])
# print(response) -> Does not exist
# response = send_request('doc', [])
# print(response) -> Does not exist

response = send_request('get_temporary_access_token', ['ITC', 'l33#'])
token = response['result']
print(token)

with open("input.bmp", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")


response = send_request('hide_secret_in_image', {'access_token':token, 'image': encoded_image })
print(response)
# -->Error: rpc_function(*positional_params, **named_params)\nTypeError: hide_secret_in_image() got an unexpected keyword argument \'image\'\n'}}


#image = base64.b64decode(response['result'].replace('\n', ''))
#with open("output.bmp", "wb") as image_file:
#   image_file.write(image)
#
#print(encoded_image)
