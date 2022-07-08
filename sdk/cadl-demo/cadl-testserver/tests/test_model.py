# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from cadl.testserver.models import PostInput


def test_model():
    model1 = PostInput(url="https://url.com")
    assert model1.url == model1["url"] == "https://url.com"

    model2 = PostInput(
        {
            "url": "https://url.com"
        }
    )
    assert model2.url == model2["url"] == "https://url.com"
