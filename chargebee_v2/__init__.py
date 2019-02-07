from chargebee_v2.api_error import APIError,PaymentError,InvalidRequestError,OperationFailedError
from chargebee_v2.models import *
from chargebee_v2.main import ChargeBee


def configure(api_key, site):
    ChargeBee.configure({
        'api_key': api_key,
        'site': site,
    })
