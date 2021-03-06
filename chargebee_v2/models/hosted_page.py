import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class HostedPage(Model):

    fields = ["id", "type", "url", "state", "failure_reason", "pass_thru_content", "embed", \
    "created_at", "expires_at", "updated_at", "resource_version", "checkout_info"]

    @property
    def content(self):
        from chargebee_v2 import Content
        if 'content' in self.values:
            return Content(self.values['content'])
        return None

    @staticmethod
    def checkout_new(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","checkout_new"), params, env, headers)

    @staticmethod
    def checkout_existing(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","checkout_existing"), params, env, headers)

    @staticmethod
    def update_card(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","update_card"), params, env, headers)

    @staticmethod
    def update_payment_method(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","update_payment_method"), params, env, headers)

    @staticmethod
    def manage_payment_sources(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","manage_payment_sources"), params, env, headers)

    @staticmethod
    def collect_now(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","collect_now"), params, env, headers)

    @staticmethod
    def extend_subscription(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","extend_subscription"), params, env, headers)

    @staticmethod
    def checkout_gift(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","checkout_gift"), params, env, headers)

    @staticmethod
    def claim_gift(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","claim_gift"), params, env, headers)

    @staticmethod
    def retrieve_agreement_pdf(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","retrieve_agreement_pdf"), params, env, headers)

    @staticmethod
    def acknowledge(id, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages",id,"acknowledge"), None, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("hosted_pages",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("hosted_pages"), params, env, headers)
