# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.automanage import AutomanageClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-automanage
# USAGE
    python create_or_update_configuration_profile.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AutomanageClient(
        credential=DefaultAzureCredential(),
        subscription_id="mySubscriptionId",
    )

    response = client.configuration_profiles.create_or_update(
        configuration_profile_name="customConfigurationProfile",
        resource_group_name="myResourceGroupName",
        parameters={
            "location": "East US",
            "properties": {
                "configuration": {
                    "Antimalware/Enable": False,
                    "AzureSecurityCenter/Enable": True,
                    "Backup/Enable": False,
                    "BootDiagnostics/Enable": True,
                    "ChangeTrackingAndInventory/Enable": True,
                    "GuestConfiguration/Enable": True,
                    "LogAnalytics/Enable": True,
                    "UpdateManagement/Enable": True,
                    "VMInsights/Enable": True,
                }
            },
            "tags": {"Organization": "Administration"},
        },
    )
    print(response)


# x-ms-original-file: specification/automanage/resource-manager/Microsoft.Automanage/stable/2022-05-04/examples/createOrUpdateConfigurationProfile.json
if __name__ == "__main__":
    main()
