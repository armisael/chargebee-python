import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class SubscriptionEstimate(Model):
    class ShippingAddress(Model):
      fields = ["first_name", "last_name", "email", "company", "phone", "line1", "line2", "line3", "city", "state_code", "state", "country", "zip", "validation_status"]
      pass

    fields = ["id", "currency_code", "status", "next_billing_at", "pause_date", "resume_date", \
    "shipping_address"]

