# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.2.1, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import DataSourcesOperations
from ._operations import IndexersOperations
from ._operations import SkillsetsOperations
from ._operations import SynonymMapsOperations
from ._operations import IndexesOperations
from ._operations import AliasesOperations
from ._operations import SearchServiceClientOperationsMixin

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DataSourcesOperations",
    "IndexersOperations",
    "SkillsetsOperations",
    "SynonymMapsOperations",
    "IndexesOperations",
    "AliasesOperations",
    "SearchServiceClientOperationsMixin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
