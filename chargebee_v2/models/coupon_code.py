import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class CouponCode(Model):

    fields = ["code", "status", "coupon_id", "coupon_set_id", "coupon_set_name"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("coupon_codes"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("coupon_codes",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("coupon_codes"), params, env, headers)

    @staticmethod
    def archive(id, env=None, headers=None):
        return request.send('post', request.uri_path("coupon_codes",id,"archive"), None, env, headers)
