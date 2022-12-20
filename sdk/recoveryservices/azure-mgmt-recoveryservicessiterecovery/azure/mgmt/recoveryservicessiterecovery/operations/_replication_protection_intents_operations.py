# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_name: str,
    resource_group_name: str,
    subscription_id: str,
    *,
    skip_token: Optional[str] = None,
    take_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip_token is not None:
        _params["skipToken"] = _SERIALIZER.query("skip_token", skip_token, "str")
    if take_token is not None:
        _params["takeToken"] = _SERIALIZER.query("take_token", take_token, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    intent_object_name: str, resource_name: str, resource_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "intentObjectName": _SERIALIZER.url("intent_object_name", intent_object_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(
    intent_object_name: str, resource_name: str, resource_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "intentObjectName": _SERIALIZER.url("intent_object_name", intent_object_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class ReplicationProtectionIntentsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicessiterecovery.SiteRecoveryManagementClient`'s
        :attr:`replication_protection_intents` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, skip_token: Optional[str] = None, take_token: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.ReplicationProtectionIntent"]:
        """Gets the list of replication protection intent objects.

        Gets the list of ASR replication protection intent objects in the vault.

        :param skip_token: The pagination token. Default value is None.
        :type skip_token: str
        :param take_token: The page size. Default value is None.
        :type take_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ReplicationProtectionIntent or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.recoveryservicessiterecovery.models.ReplicationProtectionIntent]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-10-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.ReplicationProtectionIntentCollection] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_name=self._config.resource_name,
                    resource_group_name=self._config.resource_group_name,
                    subscription_id=self._config.subscription_id,
                    skip_token=skip_token,
                    take_token=take_token,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ReplicationProtectionIntentCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents"
    }

    @distributed_trace
    def get(self, intent_object_name: str, **kwargs: Any) -> _models.ReplicationProtectionIntent:
        """Gets the details of a Replication protection intent item.

        Gets the details of an ASR replication protection intent.

        :param intent_object_name: Replication protection intent name. Required.
        :type intent_object_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReplicationProtectionIntent or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicessiterecovery.models.ReplicationProtectionIntent
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-10-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.ReplicationProtectionIntent] = kwargs.pop("cls", None)

        request = build_get_request(
            intent_object_name=intent_object_name,
            resource_name=self._config.resource_name,
            resource_group_name=self._config.resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ReplicationProtectionIntent", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}"
    }

    @overload
    def create(
        self,
        intent_object_name: str,
        input: _models.CreateProtectionIntentInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ReplicationProtectionIntent:
        """Create protection intent Resource.

        The operation to create an ASR replication protection intent item.

        :param intent_object_name: A name for the replication protection item. Required.
        :type intent_object_name: str
        :param input: Create Protection Intent Input. Required.
        :type input: ~azure.mgmt.recoveryservicessiterecovery.models.CreateProtectionIntentInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReplicationProtectionIntent or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicessiterecovery.models.ReplicationProtectionIntent
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, intent_object_name: str, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReplicationProtectionIntent:
        """Create protection intent Resource.

        The operation to create an ASR replication protection intent item.

        :param intent_object_name: A name for the replication protection item. Required.
        :type intent_object_name: str
        :param input: Create Protection Intent Input. Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReplicationProtectionIntent or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicessiterecovery.models.ReplicationProtectionIntent
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self, intent_object_name: str, input: Union[_models.CreateProtectionIntentInput, IO], **kwargs: Any
    ) -> _models.ReplicationProtectionIntent:
        """Create protection intent Resource.

        The operation to create an ASR replication protection intent item.

        :param intent_object_name: A name for the replication protection item. Required.
        :type intent_object_name: str
        :param input: Create Protection Intent Input. Is either a model type or a IO type. Required.
        :type input: ~azure.mgmt.recoveryservicessiterecovery.models.CreateProtectionIntentInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReplicationProtectionIntent or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicessiterecovery.models.ReplicationProtectionIntent
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-10-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ReplicationProtectionIntent] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _json = self._serialize.body(input, "CreateProtectionIntentInput")

        request = build_create_request(
            intent_object_name=intent_object_name,
            resource_name=self._config.resource_name,
            resource_group_name=self._config.resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ReplicationProtectionIntent", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectionIntents/{intentObjectName}"
    }
