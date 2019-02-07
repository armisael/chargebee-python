import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class Address(Model):

    fields = ["label", "first_name", "last_name", "email", "company", "phone", "addr", "extended_addr", \
    "extended_addr2", "city", "state_code", "state", "country", "zip", "validation_status", "subscription_id"]


    @staticmethod
    def retrieve(params, env=None, headers=None):
        return request.send('get', request.uri_path("addresses"), params, env, headers)

    @staticmethod
    def update(params, env=None, headers=None):
        return request.send('post', request.uri_path("addresses"), params, env, headers)
