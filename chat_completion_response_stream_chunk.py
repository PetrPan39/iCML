# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .shared.content_delta import ContentDelta

__all__ = ["ChatCompletionResponseStreamChunk", "Event", "Metric"]


class Event(BaseModel):
    delta: ContentDelta
    """Content generated since last event.

    This can be one or more tokens, or a tool call.
    """

    event_type: Literal["start", "complete", "progress"]
    """Type of the event"""

    logprobs: Optional[List[TokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None
    """Optional reason why generation stopped, if complete"""


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[str, float, bool, None]]] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: Event
    """The event containing the new content"""

    metrics: Optional[List[Metric]] = None
