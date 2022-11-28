# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datafactory
# USAGE
    python data_flows_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataFactoryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="12345678-1234-1234-1234-12345678abc",
    )

    response = client.data_flows.create_or_update(
        resource_group_name="exampleResourceGroup",
        factory_name="exampleFactoryName",
        data_flow_name="exampleDataFlow",
        data_flow={
            "properties": {
                "description": "Sample demo data flow to convert currencies showing usage of union, derive and conditional split transformation.",
                "type": "MappingDataFlow",
                "typeProperties": {
                    "scriptLines": [
                        "source(output(",
                        "PreviousConversionRate as double,",
                        "Country as string,",
                        "DateTime1 as string,",
                        "CurrentConversionRate as double",
                        "),",
                        "allowSchemaDrift: false,",
                        "validateSchema: false) ~> USDCurrency",
                        "source(output(",
                        "PreviousConversionRate as double,",
                        "Country as string,",
                        "DateTime1 as string,",
                        "CurrentConversionRate as double",
                        "),",
                        "allowSchemaDrift: true,",
                        "validateSchema: false) ~> CADSource",
                        "USDCurrency, CADSource union(byName: true)~> Union",
                        "Union derive(NewCurrencyRate = round(CurrentConversionRate*1.25)) ~> NewCurrencyColumn",
                        "NewCurrencyColumn split(Country == 'USD',",
                        "Country == 'CAD',disjoint: false) ~> ConditionalSplit1@(USD, CAD)",
                        "ConditionalSplit1@USD sink(saveMode:'overwrite' ) ~> USDSink",
                        "ConditionalSplit1@CAD sink(saveMode:'overwrite' ) ~> CADSink",
                    ],
                    "sinks": [
                        {"dataset": {"referenceName": "USDOutput", "type": "DatasetReference"}, "name": "USDSink"},
                        {"dataset": {"referenceName": "CADOutput", "type": "DatasetReference"}, "name": "CADSink"},
                    ],
                    "sources": [
                        {
                            "dataset": {"referenceName": "CurrencyDatasetUSD", "type": "DatasetReference"},
                            "name": "USDCurrency",
                        },
                        {
                            "dataset": {"referenceName": "CurrencyDatasetCAD", "type": "DatasetReference"},
                            "name": "CADSource",
                        },
                    ],
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/datafactory/resource-manager/Microsoft.DataFactory/stable/2018-06-01/examples/DataFlows_Update.json
if __name__ == "__main__":
    main()
