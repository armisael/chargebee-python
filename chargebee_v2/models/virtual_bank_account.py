import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class VirtualBankAccount(Model):

    fields = ["id", "customer_id", "email", "bank_name", "account_number", "routing_number", \
    "swift_code", "gateway", "gateway_account_id", "reference_id", "deleted"]


    @staticmethod
    def create_using_permanent_token(params, env=None, headers=None):
        return request.send('post', request.uri_path("virtual_bank_accounts","create_using_permanent_token"), params, env, headers)

    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("virtual_bank_accounts"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("virtual_bank_accounts",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("virtual_bank_accounts"), params, env, headers)
