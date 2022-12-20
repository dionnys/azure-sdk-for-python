# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
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


def build_purge_request(
    resource_group_name: str, workspace_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-08-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/purge",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_purge_status_request(
    resource_group_name: str, workspace_name: str, purge_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2020-08-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/operations/{purgeId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
        "purgeId": _SERIALIZER.url("purge_id", purge_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class WorkspacePurgeOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.loganalytics.LogAnalyticsManagementClient`'s
        :attr:`workspace_purge` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def purge(
        self,
        resource_group_name: str,
        workspace_name: str,
        body: _models.WorkspacePurgeBody,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspacePurgeResponse:
        """Purges data in an Log Analytics workspace by a set of user-defined filters.

        In order to manage system resources, purge requests are throttled at 50 requests per hour. You
        should batch the execution of purge requests by sending a single command whose predicate
        includes all user identities that require purging. Use the in operator to specify multiple
        identities. You should run the query prior to using for a purge request to verify that the
        results are expected.
        Log Analytics only supports purge operations required for compliance with GDPR. The Log
        Analytics product team reserves the right to reject requests for purge operations that are not
        for the purpose of GDPR compliance. In the event of a dispute, please create a support ticket.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param body: Describes the body of a request to purge data in a single table of an Log
         Analytics Workspace. Required.
        :type body: ~azure.mgmt.loganalytics.models.WorkspacePurgeBody
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspacePurgeResponse or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.WorkspacePurgeResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def purge(
        self,
        resource_group_name: str,
        workspace_name: str,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkspacePurgeResponse:
        """Purges data in an Log Analytics workspace by a set of user-defined filters.

        In order to manage system resources, purge requests are throttled at 50 requests per hour. You
        should batch the execution of purge requests by sending a single command whose predicate
        includes all user identities that require purging. Use the in operator to specify multiple
        identities. You should run the query prior to using for a purge request to verify that the
        results are expected.
        Log Analytics only supports purge operations required for compliance with GDPR. The Log
        Analytics product team reserves the right to reject requests for purge operations that are not
        for the purpose of GDPR compliance. In the event of a dispute, please create a support ticket.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param body: Describes the body of a request to purge data in a single table of an Log
         Analytics Workspace. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspacePurgeResponse or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.WorkspacePurgeResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def purge(
        self, resource_group_name: str, workspace_name: str, body: Union[_models.WorkspacePurgeBody, IO], **kwargs: Any
    ) -> _models.WorkspacePurgeResponse:
        """Purges data in an Log Analytics workspace by a set of user-defined filters.

        In order to manage system resources, purge requests are throttled at 50 requests per hour. You
        should batch the execution of purge requests by sending a single command whose predicate
        includes all user identities that require purging. Use the in operator to specify multiple
        identities. You should run the query prior to using for a purge request to verify that the
        results are expected.
        Log Analytics only supports purge operations required for compliance with GDPR. The Log
        Analytics product team reserves the right to reject requests for purge operations that are not
        for the purpose of GDPR compliance. In the event of a dispute, please create a support ticket.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param body: Describes the body of a request to purge data in a single table of an Log
         Analytics Workspace. Is either a model type or a IO type. Required.
        :type body: ~azure.mgmt.loganalytics.models.WorkspacePurgeBody or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspacePurgeResponse or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.WorkspacePurgeResponse
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

        api_version: Literal["2020-08-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.WorkspacePurgeResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "WorkspacePurgeBody")

        request = build_purge_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.purge.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["x-ms-status-location"] = self._deserialize(
            "str", response.headers.get("x-ms-status-location")
        )

        deserialized = self._deserialize("WorkspacePurgeResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    purge.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/purge"
    }

    @distributed_trace
    def get_purge_status(
        self, resource_group_name: str, workspace_name: str, purge_id: str, **kwargs: Any
    ) -> _models.WorkspacePurgeStatusResponse:
        """Gets status of an ongoing purge operation.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param purge_id: In a purge status request, this is the Id of the operation the status of which
         is returned. Required.
        :type purge_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspacePurgeStatusResponse or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.WorkspacePurgeStatusResponse
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

        api_version: Literal["2020-08-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        cls: ClsType[_models.WorkspacePurgeStatusResponse] = kwargs.pop("cls", None)

        request = build_get_purge_status_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            purge_id=purge_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_purge_status.metadata["url"],
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

        deserialized = self._deserialize("WorkspacePurgeStatusResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_purge_status.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/operations/{purgeId}"
    }
