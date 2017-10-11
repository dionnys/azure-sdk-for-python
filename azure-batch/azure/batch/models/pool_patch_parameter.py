# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PoolPatchParameter(Model):
    """The set of changes to be made to a pool.

    :param start_task: A task to run on each compute node as it joins the
     pool. The task runs when the node is added to the pool or when the node is
     restarted. If this element is present, it overwrites any existing start
     task. If omitted, any existing start task is left unchanged.
    :type start_task: ~azure.batch.models.StartTask
    :param certificate_references: A list of certificates to be installed on
     each compute node in the pool. If this element is present, it replaces any
     existing certificate references configured on the pool. If omitted, any
     existing certificate references are left unchanged. For Windows compute
     nodes, the Batch service installs the certificates to the specified
     certificate store and location. For Linux compute nodes, the certificates
     are stored in a directory inside the task working directory and an
     environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to
     query for this location. For certificates with visibility of 'remoteUser',
     a 'certs' directory is created in the user's home directory (e.g.,
     /home/{user-name}/certs) and certificates are placed in that directory.
    :type certificate_references:
     list[~azure.batch.models.CertificateReference]
    :param application_package_references: A list of application packages to
     be installed on each compute node in the pool. Changes to application
     package references affect all new compute nodes joining the pool, but do
     not affect compute nodes that are already in the pool until they are
     rebooted or reimaged. If this element is present, it replaces any existing
     application package references. If you specify an empty collection, then
     all application package references are removed from the pool. If omitted,
     any existing application package references are left unchanged.
    :type application_package_references:
     list[~azure.batch.models.ApplicationPackageReference]
    :param metadata: A list of name-value pairs associated with the pool as
     metadata. If this element is present, it replaces any existing metadata
     configured on the pool. If you specify an empty collection, any metadata
     is removed from the pool. If omitted, any existing metadata is left
     unchanged.
    :type metadata: list[~azure.batch.models.MetadataItem]
    """

    _attribute_map = {
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, start_task=None, certificate_references=None, application_package_references=None, metadata=None):
        self.start_task = start_task
        self.certificate_references = certificate_references
        self.application_package_references = application_package_references
        self.metadata = metadata
