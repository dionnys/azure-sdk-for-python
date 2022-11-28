# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Required for storage accounts where kind = BlobStorage. The access tier used for billing."""

    HOT = "Hot"
    COOL = "Cool"


class AccountStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status indicating whether the primary location of the storage account is available or
    unavailable.
    """

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class Bypass(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are
    any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to
    bypass none of those traffics.
    """

    NONE = "None"
    LOGGING = "Logging"
    METRICS = "Metrics"
    AZURE_SERVICES = "AzureServices"


class CorsRuleAllowedMethodsItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CorsRuleAllowedMethodsItem."""

    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    MERGE = "MERGE"
    POST = "POST"
    OPTIONS = "OPTIONS"
    PUT = "PUT"


class DefaultAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the default action of allow or deny when no other rules match."""

    ALLOW = "Allow"
    DENY = "Deny"


class Enum8(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum8."""

    DEFAULT = "default"


class GeoReplicationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the secondary location. Possible values are: - Live: Indicates that the secondary
    location is active and operational. - Bootstrap: Indicates initial synchronization from the
    primary location to the secondary location is in progress.This typically occurs when
    replication is first enabled. - Unavailable: Indicates that the secondary location is
    temporarily unavailable.
    """

    LIVE = "Live"
    BOOTSTRAP = "Bootstrap"
    UNAVAILABLE = "Unavailable"


class HttpProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol permitted for a request made with the account SAS."""

    HTTPS_HTTP = "https,http"
    HTTPS = "https"


class ImmutabilityPolicyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ImmutabilityPolicy state of a blob container, possible values include: Locked and Unlocked."""

    LOCKED = "Locked"
    UNLOCKED = "Unlocked"


class ImmutabilityPolicyUpdateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ImmutabilityPolicy update type of a blob container, possible values include: put, lock and
    extend.
    """

    PUT = "put"
    LOCK = "lock"
    EXTEND = "extend"


class KeyPermission(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Permissions for the key -- read-only or full permissions."""

    READ = "Read"
    FULL = "Full"


class KeySource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage,
    Microsoft.Keyvault.
    """

    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of storage account."""

    STORAGE = "Storage"
    STORAGE_V2 = "StorageV2"
    BLOB_STORAGE = "BlobStorage"
    FILE_STORAGE = "FileStorage"
    BLOCK_BLOB_STORAGE = "BlockBlobStorage"


class LeaseContainerRequestAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the lease action. Can be one of the available actions."""

    ACQUIRE = "Acquire"
    RENEW = "Renew"
    CHANGE = "Change"
    RELEASE = "Release"
    BREAK = "Break"


class LeaseDuration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether the lease on a container is of infinite or fixed duration, only when the
    container is leased.
    """

    INFINITE = "Infinite"
    FIXED = "Fixed"


class LeaseState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Lease state of the container."""

    AVAILABLE = "Available"
    LEASED = "Leased"
    EXPIRED = "Expired"
    BREAKING = "Breaking"
    BROKEN = "Broken"


class LeaseStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The lease status of the container."""

    LOCKED = "Locked"
    UNLOCKED = "Unlocked"


class ManagementPolicyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ManagementPolicyName."""

    DEFAULT = "default"


class Permissions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed permissions for the account SAS. Possible values include: Read (r), Write (w),
    Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p).
    """

    R = "r"
    D = "d"
    W = "w"
    L = "l"
    A = "a"
    C = "c"
    U = "u"
    P = "p"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status of the storage account at the time the operation was called."""

    CREATING = "Creating"
    RESOLVING_DNS = "ResolvingDNS"
    SUCCEEDED = "Succeeded"


class PublicAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether data in the container may be accessed publicly and the level of access."""

    CONTAINER = "Container"
    BLOB = "Blob"
    NONE = "None"


class Reason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the reason that a storage account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    ACCOUNT_NAME_INVALID = "AccountNameInvalid"
    ALREADY_EXISTS = "AlreadyExists"


class ReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". Quota Id is set when the SKU has requiredQuotas parameter as the
    subscription does not belong to that quota. The "NotAvailableForSubscription" is related to
    capacity at DC.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class Services(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed services accessible with the account SAS. Possible values include: Blob (b), Queue
    (q), Table (t), File (f).
    """

    B = "b"
    Q = "q"
    T = "t"
    F = "f"


class SignedResource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed services accessible with the service SAS. Possible values include: Blob (b),
    Container (c), File (f), Share (s).
    """

    B = "b"
    C = "c"
    F = "f"
    S = "s"


class SignedResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed resource types that are accessible with the account SAS. Service (s): Access to
    service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to
    object-level APIs for blobs, queue messages, table entities, and files.
    """

    S = "s"
    C = "c"
    O = "o"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the SKU name. Required for account creation; optional for update. Note that in
    older versions, SKU name was called accountType.
    """

    STANDARD_LRS = "Standard_LRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_RAGRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
    PREMIUM_ZRS = "Premium_ZRS"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the SKU tier. This is based on the SKU name."""

    STANDARD = "Standard"
    PREMIUM = "Premium"


class State(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the state of virtual network rule."""

    PROVISIONING = "provisioning"
    DEPROVISIONING = "deprovisioning"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    NETWORK_SOURCE_DELETED = "networkSourceDeleted"


class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the unit of measurement."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNTS_PER_SECOND = "CountsPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
