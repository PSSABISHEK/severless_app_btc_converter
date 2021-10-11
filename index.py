import requests
from requests.exceptions import HTTPError

def main(params):
    if "currency" not in params:
        return { "error": "Missing mandatory argument: currency" }
    if "amount" not in params:
        return { "error": "Missing mandatory argument: amount" }

    curr = params["currency"]
    amt = params["amount"]

    try:
        if params['currency'] not in ["GBP", "EUR", "USD"]:
            convert_json = requests.get('https://free.currconv.com/api/v7/convert?q='+params['currency']+'_USD&compact=y&apiKey=efbb179375f2bb73bea2')
            convert_json.raise_for_status()
            convert_json = convert_json.json()
            value = convert_json[params['currency']+'_USD']['val'] * params["amount"]
            curr = "USD"
            amt = value
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/'+curr+'.json')
        response.raise_for_status()
        response = response.json()
        cost = response["bpi"][curr]["rate"]
        cost = cost.replace(',','')
        cost = amt / float(cost)
        cost = "{:.4f}".format(cost)
        return {"amount": cost, "message": ""+str(params["amount"])+" "+str(params["currency"])+" is worth "+str(cost)+" bitcoins"}
        

    except HTTPError as http_err:
        return (f'HTTP error occurred: {http_err}')
    except Exception as err:
        return (f'Other error occurred: {err}')

# UNCOMMNET TO BELOW TO RUN LOCALLY
# if __name__ == "__main__":
#     main({"currency": "PHP", "amount": 1000})