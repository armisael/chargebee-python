import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class ShippingAddress(Model):

    fields = ["label", "first_name", "last_name", "email", "company", "phone", "addr", "extended_addr", \
    "extended_addr2", "city", "state", "country", "zip", "subscription_id"]


    @staticmethod
    def retrieve(params, env=None):
        return request.send('get', '/shipping_addresses', params, env)

    @staticmethod
    def update(params, env=None):
        return request.send('post', '/shipping_addresses', params, env)
