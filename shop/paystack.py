import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()
 

secret_key = os.environ.get('paystack')
url='https://api.paystack.co/transaction/initialize'

headers = {
    "Authorization": f'Bearer {secret_key}',
"Content-Type": "application/json"
}
data={ 
  "email": "komo2success21@gmail.com", 
  "amount": 20000,
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
# django in production does not serve static files and media file in production
# whitenoise will serve in media file and not in static files
# url = "https://dummyjson.com/products"
# response = requests.get(url)
# print ()
# print('response.get')
# status coe and their meaning
# 200=successful
# 201 =created
# 301 = redirect
# 400 = bad request
# 403= forbidden 
# 404 = Not found
# 405 = unauthorize
# 500 = generic error response

# Http method
# 1.get
# 2.post
# 3.put
# 4.delete
# 5.update

# data structure
# dictionary- key word attribute 
# fruit = {'name':'apple'}
# print ['name']
# pr
# if response.status_code == 200:
#     data = response.json()
#     for product in data['products']:
#         id = product['id']
#         title = product['title']
#         price = product['price']
#         weight = product['weight']

#         print(f" {id} the price of {title} is ₦ {price} with weight of {weight}")
        
def paystack(email, amount):
    url='https://api.paystack.co/transaction/initialize'
    headers = {
    "Authorization": f'Bearer {secret_key}',
    "Content-Type": "application/json"
    }
    data={ 
    "email": email, 
    "amount": amount * 100
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    data = response.json()
    return data