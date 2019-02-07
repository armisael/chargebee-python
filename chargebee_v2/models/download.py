import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class Download(Model):

    fields = ["download_url", "valid_till"]

