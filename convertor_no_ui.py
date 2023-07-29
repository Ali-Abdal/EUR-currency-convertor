import requests

base_url = 'http://api.exchangeratesapi.io/v1/latest'
access_key = 'your key' 
currency = input('Convert from EUR to (currency):\n> ')
quantity = float(input(f"How much EUR do you want to convert:\n> "))

full_url = base_url + '?' + access_key + '&symbols=' + currency

response = requests.get(full_url)

if response.ok:
    data = response.json()
    rate = data['rates'][currency]

    result = quantity * rate
    
    print(f"\n{quantity} EUR is equal to {round(result,2)} {currency}")

else:
    print(f"Error {response.status_code}")
    print(response.json()['error']['message'])
