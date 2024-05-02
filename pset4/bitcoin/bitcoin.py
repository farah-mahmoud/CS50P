#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        print("Missing Command-line argument")
        sys.exit(1)

    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    #print(json.dumps(res.json(), indent=2)) #makes the response readable

    data = res.json()
    if "bpi" in data:
        USD_Rate = data['bpi']['USD']['rate_float']
        Amount = USD_Rate * float(sys.argv[1])
        print(f"${Amount:,.4f}")
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except requests.RequestException:
    sys.exit()
