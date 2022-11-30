# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ConfidentialLedgerBugBashClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for ConfidentialLedgerBugBashClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param ledger_uri: Required.
    :type ledger_uri: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param api_version: The API version to use for this operation. Required.
    :type api_version: str
    """

    def __init__(self, ledger_uri: str, credential: "AsyncTokenCredential", api_version: str, **kwargs: Any) -> None:
        super(ConfidentialLedgerBugBashClientConfiguration, self).__init__(**kwargs)
        if ledger_uri is None:
            raise ValueError("Parameter 'ledger_uri' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if api_version is None:
            raise ValueError("Parameter 'api_version' must not be None.")

        self.ledger_uri = ledger_uri
        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://confidential-ledger.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "security-confidentialledgerbugbash/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
