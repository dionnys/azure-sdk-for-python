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
from .._vendor import ManagementGroupsAPIMixinABC, _convert_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_check_name_availability_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: Literal["2021-04-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Management/checkNameAvailability")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_start_tenant_backfill_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: Literal["2021-04-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Management/startTenantBackfill")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_tenant_backfill_status_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-04-01"))  # type: Literal["2021-04-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Management/tenantBackfillStatus")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ManagementGroupsAPIOperationsMixin(ManagementGroupsAPIMixinABC):
    @overload
    def check_name_availability(
        self,
        check_name_availability_request: _models.CheckNameAvailabilityRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityResult:
        """Checks if the specified management group name is valid and unique.

        :param check_name_availability_request: Management group name availability check parameters.
         Required.
        :type check_name_availability_request:
         ~azure.mgmt.managementgroups.models.CheckNameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.CheckNameAvailabilityResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_name_availability(
        self, check_name_availability_request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResult:
        """Checks if the specified management group name is valid and unique.

        :param check_name_availability_request: Management group name availability check parameters.
         Required.
        :type check_name_availability_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.CheckNameAvailabilityResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_name_availability(
        self, check_name_availability_request: Union[_models.CheckNameAvailabilityRequest, IO], **kwargs: Any
    ) -> _models.CheckNameAvailabilityResult:
        """Checks if the specified management group name is valid and unique.

        :param check_name_availability_request: Management group name availability check parameters. Is
         either a model type or a IO type. Required.
        :type check_name_availability_request:
         ~azure.mgmt.managementgroups.models.CheckNameAvailabilityRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.CheckNameAvailabilityResult
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-04-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CheckNameAvailabilityResult]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_request, (IO, bytes)):
            _content = check_name_availability_request
        else:
            _json = self._serialize.body(check_name_availability_request, "CheckNameAvailabilityRequest")

        request = build_check_name_availability_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {"url": "/providers/Microsoft.Management/checkNameAvailability"}  # type: ignore

    @distributed_trace
    def start_tenant_backfill(self, **kwargs: Any) -> _models.TenantBackfillStatusResult:
        """Starts backfilling subscriptions for the Tenant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantBackfillStatusResult or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.TenantBackfillStatusResult
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-04-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.TenantBackfillStatusResult]

        request = build_start_tenant_backfill_request(
            api_version=api_version,
            template_url=self.start_tenant_backfill.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TenantBackfillStatusResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    start_tenant_backfill.metadata = {"url": "/providers/Microsoft.Management/startTenantBackfill"}  # type: ignore

    @distributed_trace
    def tenant_backfill_status(self, **kwargs: Any) -> _models.TenantBackfillStatusResult:
        """Gets tenant backfill status.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantBackfillStatusResult or the result of cls(response)
        :rtype: ~azure.mgmt.managementgroups.models.TenantBackfillStatusResult
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-04-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.TenantBackfillStatusResult]

        request = build_tenant_backfill_status_request(
            api_version=api_version,
            template_url=self.tenant_backfill_status.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TenantBackfillStatusResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    tenant_backfill_status.metadata = {"url": "/providers/Microsoft.Management/tenantBackfillStatus"}  # type: ignore
