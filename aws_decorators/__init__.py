import os
from functools import wraps
from inspect import getargspec

import boto3
from boto3.session import Session

AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')


def get_session(*args, **kwargs):
    """
    Optional parameters:

    See the boto3 _documentation

    :param aws_access_key_id: AWS access key ID
    :type aws_access_key_id: string
    :param aws_secret_access_key: AWS secret access key
    :type aws_secret_access_key: string
    :param aws_session_token: AWS temporary session token
    :type aws_session_token: string
    :param region_name: Default region when creating new connections
    :type region_name: string
    :param botocore_session: Use this Botocore session instead of creating a new default one
    :type botocore_session: botocore.session.Session
    :param profile_name: The name of a profile to use. If not given, then the default profile is used.
    :type profile_name: string

    .. _documentation: http://boto3.readthedocs.io/en/latest/reference/core/session.html
    """
    return Session(**kwargs)


def get_client(name, client_type='client', region=None, session=None, *args, **kwargs):
    """Helper function to get a boto3 client for a service.

    :param name: **required**.
    :type name: string
    :param client_type: Can be resource or client. Defaults to ``client``

        * client returns an instance of _boto3.session.Session.client
        * resource returns an instance of _boto3.session.Session.resource

    :type client_type: string
    :param region: Depricated. Use region_name. The name of the region associated with the client.
    :type region: string
    :param session: session
    :type session: boto3.session.Session

    Optional parameters:

        * region_name: string
        * api_version: string
        * use_ssl: boolean
        * verify: boolean/string
        * endpoint_url: string
        * aws_access_key_id: string
        * aws_secret_access_key: string
        * aws_session_token: string
        * config: _botocore.client.Config

    .. _boto3.session.Session.resource: http://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.resource
    .. _boto3.session.Session.client: http://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client
    .. _botocore.client.Config: https://botocore.readthedocs.io/en/latest/reference/config.html
    """
    kwargs['name'] = name
    if region is not None:
        kwargs['region_name'] = region
    if session is None:
        session = boto3
    fn = getattr(session, client_type)
    return fn(**kwargs)


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
