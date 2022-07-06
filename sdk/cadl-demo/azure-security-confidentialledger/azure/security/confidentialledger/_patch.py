# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies
from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import ConfidentialLedgerServiceConfiguration
from ._serialization import Deserializer, Serializer
from .operations import ConfidentialLedger, ConfidentialLedgerIdentityService
from ._client import ConfidentialLedgerService as ConfidentialLedgerServiceGenerated

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential
    from typing import Dict
from ._version import VERSION


class ConfidentialLedgerServiceConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for ConfidentialLedgerService.

    Note that all parameters used to create this instance are saved as instance
    attributes.
    """

    def __init__(self, endpoint: str, credential: "TokenCredential", **kwargs: Any) -> None:
        super(ConfidentialLedgerServiceConfiguration, self).__init__(**kwargs)

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://confidential-ledger.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "security-confidentialledger/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(
            self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )


class ConfidentialLedgerService(ConfidentialLedgerServiceGenerated):
    """Service client

    :ivar confidential_ledger: ConfidentialLedger operations
    :vartype confidential_ledger: azure.security.confidentialledger.operations.ConfidentialLedger
    :ivar confidential_ledger_identity_service: ConfidentialLedgerIdentityService operations
    :vartype confidential_ledger_identity_service:
     azure.security.confidentialledger.operations.ConfidentialLedgerIdentityService
    :keyword endpoint: Service host Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(self, credential: "Tokencredential", *, endpoint: str, **kwargs: Any) -> None:
        self._config = ConfidentialLedgerServiceConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.confidential_ledger = ConfidentialLedger(self._client, self._config, self._serialize, self._deserialize)
        self.confidential_ledger_identity_service = ConfidentialLedgerIdentityService(
            self._client, self._config, self._serialize, self._deserialize
        )


__all__ = ["ConfidentialLedgerService"]


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
