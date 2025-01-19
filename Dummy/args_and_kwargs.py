# def get_values(x, y, *args, **kwargs):
#     print(kwargs.get('name'))
#     print(args)


# get_values(4,5,6,7,88, name='sagar')

import requests

BASE_URL="http://127.0.0.1:8000/"
END_POINT="productapi"

resp=requests.get(BASE_URL+END_POINT)

data=resp.json()

print("data from django application")

print(data)

