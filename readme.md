## What does the action do ?
This action is hosted as a serverless application in IBM Cloud function. It takes a price and currency and returns a message contains the equivalent amount of Bitcoin.
This is done as an exercise from [Openwhisk Bootcamp](https://github.com/IBM-Cloud/openwhisk-workshops/blob/master/bootcamp/ex1%20-%20creating%20and%20invoking%20actions/README.md#exercises)

## Test with currencies in the Coindeck API response.

```
$ ibmcloud wsk action invoke bitcoin -r -p amount 1000 -p currency USD
{
    "amount": "0.160814",
    "label": "1000 USD is worth 0.160814 bitcoins."
}

$ ibmcloud wsk action invoke bitcoin -r -p amount 1000 -p currency EUR
{
    "amount": "0.187235",
    "label": "1000 EUR is worth 0.187235 bitcoins."
}

$ ibmcloud wsk action invoke bitcoin -r -p amount 1000 -p currency GBP
{
    "amount": "0.213012",
    "label": "1000 GBP is worth 0.213012 bitcoins."
}
```

## Test with currencies not in the Coindeck API response.

```
$ ibmcloud wsk action invoke bitcoin -r -p amount 1000 -p currency AUD
{
    "amount": "0.10814",
    "label": "1000 AUD is worth 0.10814 bitcoins."
}
```

## Test with missing parameters.

```
$ ibmcloud wsk action invoke bitcoin -r -p amount 1000
{
    "error": "Missing mandatory argument: currency"
}

$ ibmcloud wsk action invoke bitcoin -r  -p currency GBP
{
    "error": "Missing mandatory argument: amount"
}
```