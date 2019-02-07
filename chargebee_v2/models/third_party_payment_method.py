import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class ThirdPartyPaymentMethod(Model):

    fields = ["type", "gateway", "gateway_account_id", "reference_id"]

