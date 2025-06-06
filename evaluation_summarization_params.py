# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationSummarizationParams"]


class EvaluationSummarizationParams(TypedDict, total=False):
    metrics: Required[List[Literal["rouge", "bleu"]]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]
