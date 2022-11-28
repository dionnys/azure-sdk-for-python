# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicessiterecovery
# USAGE
    python replication_protected_items_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SiteRecoveryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="c183865e-6077-46f2-a3b1-deb0f4f4650a",
        resource_group_name="resourceGroupPS1",
        resource_name="vault1",
    )

    response = client.replication_protected_items.begin_update(
        fabric_name="cloud1",
        protection_container_name="cloud_6d224fc6-f326-5d35-96de-fbf51efb3179",
        replicated_protected_item_name="f8491e4f-817a-40dd-a90c-af773978c75b",
        update_protection_input={
            "properties": {
                "licenseType": "WindowsServer",
                "providerSpecificDetails": {"instanceType": "HyperVReplicaAzure"},
                "recoveryAzureVMName": "vm1",
                "recoveryAzureVMSize": "Basic_A0",
                "selectedRecoveryAzureNetworkId": "/subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/siterecoveryProd1/providers/Microsoft.Network/virtualNetworks/vnetavrai",
                "vmNics": [
                    {
                        "ipConfigs": [
                            {
                                "ipConfigName": "ipconfig1",
                                "isPrimary": True,
                                "recoveryStaticIPAddress": "10.0.2.46",
                                "recoverySubnetName": "subnet1",
                            }
                        ],
                        "nicId": "TWljcm9zb2Z0OkY4NDkxRTRGLTgxN0EtNDBERC1BOTBDLUFGNzczOTc4Qzc1Qlw3NjAwMzMxRS03NDk4LTQ0QTQtQjdDNy0xQjY1NkJDREQ1MkQ=",
                        "selectionType": "SelectedByUser",
                    }
                ],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/stable/2022-09-10/examples/ReplicationProtectedItems_Update.json
if __name__ == "__main__":
    main()
