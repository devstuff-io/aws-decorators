import os
from functools import wraps
from inspect import getargspec

import boto3

AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')


def get_client(name, client_type='client', region=None, *args, **kwargs):
    if region is None:
        region = AWS_REGION
    fn = getattr(boto3, client_type)
    return fn(name, region_name=region, **kwargs)


def boto_client(service_name, client_type='client', region=AWS_REGION,
                client_param_name='client', region_param_name='region'):
    def _get_client(func):
        @wraps(func)
        def make_client(*args, **kwargs):
            fn_spec = getargspec(func)
            # create a dict with the fn's kwargs and default values
            params = dict(
                zip(fn_spec.args[-len(fn_spec.defaults):], fn_spec.defaults)
            )

            # update params with arg values and keys
            params.update(dict((zip(fn_spec.args[:len(args)], args))))
            params.update(kwargs)

            if params.get(region_param_name) is None:
                params[region_param_name] = region

            if params.get(client_param_name) is None:
                params[client_param_name] = get_client(
                    service_name,
                    client_type,
                    params[region_param_name]
                )

            return func(**params)
        return make_client
    return _get_client


__version__ = '0.0.8'
