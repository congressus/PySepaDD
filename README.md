#PySepaDD - Generate SEPA Direct Debit XML

PySepaDD is a python class to generate SEPA PAIN.008.001.02 compliant Direct Debit XML files. 

##Configuring

####Parameters
When intializing PySepaDD you MUST supply a config dictionary, the dictionary requires the following parameters:
* (String)  `name`       : The name of the creditor.
* (String)  `IBAN`       : The International Bank Account Number of the creditor.
* (String)  `BIC`        : The Bank Identifier Code of the creditor. 
* (Boolean) `batch`      : Whether to process in batch or non-batch mode. (Likely `True`). 
* (String)  `creditor_id`: The creditor identification. (Supplied by your bank).
* (String)  `currency`   : The creditors currency. (ISO 4217)

####Errors
The initialization will throw an `Exception` when the config does not validate. The Exception contains a concatenated string (prepended by `Config file did not validate. ` with the (capitalized) items that are missing. For example:

`Config file did not validate. NAME_MISSING BATCH_MISSING`


####Example
```python
config = {"name": "Test von Testenstein",
          "IBAN": "NL50BANK1234567890",
          "BIC": "BANKNL2A",
          "batch": True,
          "creditor_id": "000000",
          "currency": "EUR"
          }
sepa = PySepaDD(config)
```

##Adding Payments
After initializing with a config, you can add payments with the `add_payment(payment_dict)` function, for which you will have to supply a payment dictionary. 

####Parameters
The payment dictionary requires the following parameters:
* (String)        `name`           : The name of the debtor.
* (String)        `IBAN`           : The International Bank Account Number of the debtor.
* (String)        `BIC`            : The Bank Identifier Code of the debtor. 
* (Integer)       `amount`         : The amount to debit **in cents**.
* (String)        `type`           : The transaction/batch type. (FRST,RCUR,OOFF,FNAL).
* (datetime.date) `collection_date`: The creditors currency. (ISO 4217).
* (String)        `mandate_id`     : The alphanumeric mandate identifier.
* (datetime.date) `mandate_date`   : The signing date of the mandate.
* (String)        `description`    : The description for the debtor. (Max 140 char alphanumeric).

####Errors
The ```add_payments(payment_dict)``` method will throw an `Exception` when the payment does not validate. The Exception contains a concatenated string with the following (combined) possibilities:
* `AMOUNT_NOT_INTEGER`

   The amount supplied is not an integer (perhaps it is a string or float?).
* `MANDATE_DATE_INVALID_OR_NOT_DATETIME_INSTANCE`

   The mandate date is not a proper `datetime.date` instance (perhaps it is a string?).
* `COLLECTION_DATE_INVALID_OR_NOT_DATETIME_INSTANCE`

   The collection date is not a proper `datetime.date` instance (perhaps it is a string?).

####Example
```python
payment = {"name": "Test von Testenstein",
            "IBAN": "NL50BANK1234567890",
            "BIC": "BANKNL2A",
            "amount": 5000,
            "type": "RCUR",
            "collection_date": datetime.date.today(),
            "mandate_id": "1234",
            "mandate_date": datetime.date.today(),
            "description": "Test transaction"
           }
sepa.add_payment(payment)
```



##Exporting
To create the direct debit XML file, use the `export()` function. This will return a string containing the file contents.

####Example
```python
contents = sepa.export()
print contents
```

##Helpers

####`int_to_decimal_str(int)`
This will convert your integers (cents) back to a decimal string (full currency, for example Euro's) with full stop separator and no thousand separators. It will not use divisions, so there will never be floating point errors.

####`decimal_str_to_int(str)`
This will convert your decimal strings (full currency, for example Euro's) with full stop separator and no thousand separators to an integer. (cents) It will not use divisions, so there will never be floating point errors.

####`check_payment(payment_dict)`
This will check your payment dictionary, but will not throw an exception when invalid. It will return either `True` indicating that your payment is valid, or it will return a string containing error messages as mentioned in the Adding Payments section.

License
----

MIT
