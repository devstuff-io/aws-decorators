aws-decorators
==============

Helpful decorators for aws things

Documentation: https://github.com/meganlkm/aws-decorators


Installation
------------

.. code-block:: shell

   pip install aws-decorators


Decorators
----------

boto_client
...........

.. code-block:: python

    boto_client(service_name, client_type='client', region=AWS_REGION,
                client_param_name='client', region_param_name='region')


**Parameters**

+------------------------+------------------------------------------------------------+----------+-------------+
| Name                   | Description                                                | Required | Default     |
+========================+============================================================+==========+=============+
| ``service_name``       | Name of the boto3 client or resource                       | yes      |             |
+------------------------+------------------------------------------------------------+----------+-------------+
| ``client_type``        | boto3 client or resource                                   | no       | client      |
+------------------------+------------------------------------------------------------+----------+-------------+
| ``region``             | The aws region to use                                      | no       | us-east-1   |
+------------------------+------------------------------------------------------------+----------+-------------+
| ``client_param_name``  | Name of the function argument for the client or resource   | no       | client      |
+------------------------+------------------------------------------------------------+----------+-------------+
| ``region_param_name``  | Name of the function argument for the aws region name      | no       | region      |
+------------------------+------------------------------------------------------------+----------+-------------+


**Usage**

.. code-block:: python

    from aws_decorators import boto_client


    @boto_client('lambda')
    def do_something_with_lambda(client=None, region=None):
        return client.get_function(FunctionName='foo')


    @boto_client('dynamodb', client_type='resource', client_param_name='fooby')
    def do_something_with_dynamodb(fooby=None, region=None):
        return fooby.create_table(...)


Authors
-------

See contributors section on GitHub.
