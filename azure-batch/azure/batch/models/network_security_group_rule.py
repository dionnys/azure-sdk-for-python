# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NetworkSecurityGroupRule(Model):
    """A network security group rule to apply to an inbound endpoint.

    :param priority: The priority for this rule. Priorities within a pool must
     be unique and are evaluated in order of priority. The lower the number the
     higher the priority. For example, rules could be specified with order
     numbers of 150, 250, and 350. The rule with the order number of 150 takes
     precedence over the rule that has an order of 250. Allowed priorities are
     150 to 3500. If any reserved or duplicate values are provided the request
     fails with HTTP status code 400.
    :type priority: int
    :param access: The action that should be taken for a specified IP address,
     subnet range or tag. Possible values include: 'allow', 'deny'
    :type access: str or ~azure.batch.models.NetworkSecurityGroupRuleAccess
    :param source_address_prefix: The source address prefix or tag to match
     for the rule. Valid values are a single IP address (i.e. 10.10.10.10), IP
     subnet (i.e. 192.168.1.0/24), default tag, or * (for all addresses).  If
     any other values are provided the request fails with HTTP status code 400.
    :type source_address_prefix: str
    """

    _validation = {
        'priority': {'required': True},
        'access': {'required': True},
        'source_address_prefix': {'required': True},
    }

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'access': {'key': 'access', 'type': 'NetworkSecurityGroupRuleAccess'},
        'source_address_prefix': {'key': 'sourceAddressPrefix', 'type': 'str'},
    }

    def __init__(self, priority, access, source_address_prefix):
        self.priority = priority
        self.access = access
        self.source_address_prefix = source_address_prefix
