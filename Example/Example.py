from PySepaDD import PySepaDD
import datetime

config = {"name": "TestCreditor",
          "IBAN": "NL50BANK1234567890",
          "BIC": "BANKNL2A",
          "batch": True,
          "creditor_id": "000000",
          "currency": "EUR"
          }
psdd = PySepaDD(config)

payment1 = {"name": "Test von Testenstein",
            "IBAN": "NL50BANK1234567890",
            "BIC": "BANKNL2A",
            "amount": 1012,
            "type": "FRST",
            "collection_date": datetime.date.today(),
            "mandate_id": "1234",
            "mandate_date": datetime.date.today(),
            "description": "Test transaction1"
           }
payment2 = {"name": "Test du Test",
            "IBAN": "NL50BANK1234567890",
            "BIC": "BANKNL2A",
            "amount": 5000,
            "type": "RCUR",
            "collection_date": datetime.date.today(),
            "mandate_id": "1234",
            "mandate_date": datetime.date.today(),
            "description": "Test transaction2"
           }

psdd.add_payment(payment1)
psdd.add_payment(payment2)

print psdd.export()
