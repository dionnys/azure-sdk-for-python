# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.credentials import AzureKeyCredential
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ..models import _models as models
from ._configuration import BatchServiceClientConfiguration
from .operations import (
    AccountOperations,
    ApplicationOperations,
    CertificateOperations,
    ComputeNodeExtensionOperations,
    ComputeNodeOperations,
    FileOperations,
    JobOperations,
    JobScheduleOperations,
    PoolOperations,
    TaskOperations,
)


class BatchServiceClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """A client for issuing REST requests to the Azure Batch service.

    :ivar application: ApplicationOperations operations
    :vartype application: azure-batch.aio.operations.ApplicationOperations
    :ivar pool: PoolOperations operations
    :vartype pool: azure-batch.aio.operations.PoolOperations
    :ivar account: AccountOperations operations
    :vartype account: azure-batch.aio.operations.AccountOperations
    :ivar job: JobOperations operations
    :vartype job: azure-batch.aio.operations.JobOperations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure-batch.aio.operations.CertificateOperations
    :ivar file: FileOperations operations
    :vartype file: azure-batch.aio.operations.FileOperations
    :ivar job_schedule: JobScheduleOperations operations
    :vartype job_schedule: azure-batch.aio.operations.JobScheduleOperations
    :ivar task: TaskOperations operations
    :vartype task: azure-batch.aio.operations.TaskOperations
    :ivar compute_node: ComputeNodeOperations operations
    :vartype compute_node: azure-batch.aio.operations.ComputeNodeOperations
    :ivar compute_node_extension: ComputeNodeExtensionOperations operations
    :vartype compute_node_extension: azure-batch.aio.operations.ComputeNodeExtensionOperations
    :param batch_url: The base URL for all Azure Batch service requests. Required.
    :type batch_url: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :keyword api_version: Api Version. Default value is "2022-01-01.15.0". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, batch_url: str, credential: AzureKeyCredential, **kwargs: Any) -> None:
        _endpoint = "{batchUrl}"
        self._config = BatchServiceClientConfiguration(batch_url=batch_url, credential=credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.application = ApplicationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pool = PoolOperations(self._client, self._config, self._serialize, self._deserialize)
        self.account = AccountOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job = JobOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file = FileOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_schedule = JobScheduleOperations(self._client, self._config, self._serialize, self._deserialize)
        self.task = TaskOperations(self._client, self._config, self._serialize, self._deserialize)
        self.compute_node = ComputeNodeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.compute_node_extension = ComputeNodeExtensionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "batchUrl": self._serialize.url("self._config.batch_url", self._config.batch_url, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "BatchServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
