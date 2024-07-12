import json
import requests
import sys


try:
    if len(sys.argv) != 2:
        raise IndexError

    current_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    number = float(sys.argv[1])
    current_price = float(current_json["bpi"]["USD"]["rate_float"])
    value = current_price * number

except requests.RequestException:
    sys.exit("Request Exception")
except IndexError:
    sys.exit("Missing command-line argument.")
except ValueError:
    sys.exit("Command-line argument is not a number.")

else:
    print("${:,.4f}".format(value))
