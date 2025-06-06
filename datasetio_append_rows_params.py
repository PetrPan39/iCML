# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DatasetioAppendRowsParams"]


class DatasetioAppendRowsParams(TypedDict, total=False):
    dataset_id: Required[str]

    rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]
