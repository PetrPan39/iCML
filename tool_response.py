# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["ToolResponse"]


class ToolResponse(BaseModel):
    call_id: str

    content: InterleavedContent
    """A image content item"""

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]
