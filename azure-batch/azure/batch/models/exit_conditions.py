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


class ExitConditions(Model):
    """Specifies how the Batch service should respond when the task completes.

    :param exit_codes: A list of individual task exit codes and how the Batch
     service should respond to them.
    :type exit_codes: list[~azure.batch.models.ExitCodeMapping]
    :param exit_code_ranges: A list of task exit code ranges and how the Batch
     service should respond to them.
    :type exit_code_ranges: list[~azure.batch.models.ExitCodeRangeMapping]
    :param pre_processing_error: How the Batch service should respond if the
     task fails to start due to an error.
    :type pre_processing_error: ~azure.batch.models.ExitOptions
    :param file_upload_error: How the Batch service should respond if a file
     upload error occurs. If the task exited with an exit code that was
     specified via exitCodes or exitCodeRanges, and then encountered a file
     upload error, then the action specified by the exit code takes precedence.
    :type file_upload_error: ~azure.batch.models.ExitOptions
    :param default: How the Batch service should respond if the task fails
     with an exit condition not covered by any of the other properties. This
     value is used if the task exits with any nonzero exit code not listed in
     the exitCodes or exitCodeRanges collection, with a pre-processing error if
     the preProcessingError property is not present, or with a file upload
     error if the fileUploadError property is not present. If you want
     non-default behaviour on exit code 0, you must list it explicitly using
     the exitCodes or exitCodeRanges collection.
    :type default: ~azure.batch.models.ExitOptions
    """

    _attribute_map = {
        'exit_codes': {'key': 'exitCodes', 'type': '[ExitCodeMapping]'},
        'exit_code_ranges': {'key': 'exitCodeRanges', 'type': '[ExitCodeRangeMapping]'},
        'pre_processing_error': {'key': 'preProcessingError', 'type': 'ExitOptions'},
        'file_upload_error': {'key': 'fileUploadError', 'type': 'ExitOptions'},
        'default': {'key': 'default', 'type': 'ExitOptions'},
    }

    def __init__(self, exit_codes=None, exit_code_ranges=None, pre_processing_error=None, file_upload_error=None, default=None):
        self.exit_codes = exit_codes
        self.exit_code_ranges = exit_code_ranges
        self.pre_processing_error = pre_processing_error
        self.file_upload_error = file_upload_error
        self.default = default
