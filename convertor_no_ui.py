import requests


base_url = 'http://api.exchangeratesapi.io/v1'
endpoint = 'latest'
access_key = 'access_key=8ee28eec0c01266b9c8d9f53894669ce' # each acc has differant key
currency = input('Convert from EUR to (currency):\n> ')
quantity = float(input(f"How much EUR do you want to convert:\n> "))

full_url = base_url + '/' + endpoint + '?' + access_key + '&symbols=' + currency

response = requests.get(full_url)

# checks if the request is successful it prints the output if there is an error it prints a friendly error message
if response.ok:
    data = response.json()
    rate = data['rates'][currency]

    result = quantity * rate
    
    print(f"\n{quantity} EUR is equal to {round(result,2)} {currency}, based upon exchane rates on {data['date']}")

else:
    print(f"Error {response.status_code}")
    print(response.json()['error']['message'])

