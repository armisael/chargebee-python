import json
from chargebee_v2.model import Model
from chargebee_v2 import request
from chargebee_v2 import APIError

class Comment(Model):

    fields = ["id", "entity_type", "added_by", "notes", "created_at", "type", "entity_id"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("comments"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("comments",id), None, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("comments"), params, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("comments",id,"delete"), None, env, headers)
