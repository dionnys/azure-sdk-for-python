# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservices import RecoveryServicesClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservices
# USAGE
    python patch_vault_with_cmk3.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = RecoveryServicesClient(
        credential=DefaultAzureCredential(),
        subscription_id="77777777-b0c6-47a2-b37c-d8e65a629c18",
    )

    response = client.vaults.begin_update(
        resource_group_name="HelloWorld",
        vault_name="swaggerExample",
        vault={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/85bf5e8c-3084-4f42-add2-746ebb7e97b2/resourcegroups/defaultrg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/examplemsi": {}
                },
            },
            "properties": {
                "encryption": {
                    "keyVaultProperties": {
                        "keyUri": "https://cmk2xkv.vault.azure.net/keys/Key1/0767b348bb1a4c07baa6c4ec0055d2b3"
                    }
                }
            },
            "tags": {"PatchKey": "PatchKeyUpdated"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/recoveryservices/resource-manager/Microsoft.RecoveryServices/stable/2022-10-01/examples/PATCHVault_WithCMK3.json
if __name__ == "__main__":
    main()
