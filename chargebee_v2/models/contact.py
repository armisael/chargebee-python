import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class Contact(Model):

    fields = ["id", "first_name", "last_name", "email", "phone", "label", "enabled", "send_account_email", \
    "send_billing_email"]

