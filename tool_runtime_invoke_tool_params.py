# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolRuntimeInvokeToolParams"]


class ToolRuntimeInvokeToolParams(TypedDict, total=False):
    kwargs: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    tool_name: Required[str]
