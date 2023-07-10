# EUR-currency-convertor

## requires previous info about: 
dictionaries - if statements - inputs

## what they will learn if they finish the challenge:
about: api, reading api docs, requests,  urls and json

## what is the challenge?:
they will use an api that provides currency rates based on EUR
using requests we will be able to get them ( we can get all rates or only the ones we want) 
```
{'success': True, 'timestamp': 1688996884, 'base': 'EUR', 'date': '2023-07-10', 'rates': {'KWD': 0.336802}}
```
so 1 EUR = 0.336802 KWD

### so we can create a simple EUR converter to any currency we want

### 1. we need to make a free acc from this website to use their api https://exchangeratesapi.io/

### 2. we will have a key that we will need to access the api 

### 3. we import requests
```
import requests
``` 

### 4. url structure is provided in the docs: https://exchangeratesapi.io/documentation/
```
https://api.exchangeratesapi.io/v1/latest
    ? access_key = API_KEY
    & base = USD
    & symbols = GBP,JPY,EUR
```
access_key: [required] Your API Key.

base: [optional] Enter the three-letter currency code of your preferred base currency.

note: changing the base is for paid edition we will only able to use EUR

symbols:  [optional] Enter a list of comma-separated currency codes to limit output currencies.
    
### 5. we create a var to store the base url:
```
base_url = 'http://api.exchangeratesapi.io/v1/latest'
```

### 6. we create a var to store the access_key:
```
access_key = 'access_key=8ee28eec0c01266b9c8d9f53894669ce'
```

### 7. we create 2 vars (currency & quantity) to store 2 inputs from the user:
```
currency = input('Convert from EUR to (currency):\n> ')
quantity = float(input(f"How much EUR do you want to convert:\n> "))
```
### note: we will need the quantity as a float because we will multiplay it with currency rate later

### 8. we create a var to store full url:
```
full_url = base_url + '?' + access_key + '&symbols=' + currency
```

### 9. we get the data using .get() from requests and store the response in a var
```
response = requests.get(full_url)
```

### 10. we handle the error in case the user entered invalid currency name 
```
# if response code is 200 it converts then prints the result
if response.ok:
  # code here

# if response is not 200 it prints a friendly error msg
else:
  # code here
```

### 11. converting and printing the result

### we store the response in a var as a dictionary using .json()
```
data = response.json()
```

### we store currency rate in a var
```
rate = data['rates'][currency]
```

### we convert then store it in a var
```
result = quantity * rate
```

### we print the result 
```
print(f"\n{quantity} EUR is equal to {round(result,2)} {currency}")
```

### so we get:
```
if response.ok:
    data = response.json()
    rate = data['rates'][currency]

    result = quantity * rate
    
    print(f"\n{quantity} EUR is equal to {round(result,2)} {currency}")

else:
  #code here
```

### 12. friendly error msg:
```
    print(f"Error {response.status_code}")
    print(response.json()['error']['message'])
```

### so we get:

```
if response.ok:
    data = response.json()
    rate = data['rates'][currency]

    result = quantity * rate
    
    print(f"\n{quantity} EUR is equal to {round(result,2)} {currency}")

else:
    print(f"Error {response.status_code}")
    print(response.json()['error']['message'])
```
