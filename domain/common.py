"""
Common domain models reused across several API endpoints.
"""
from datetime import datetime
from enum import Enum
from typing import Annotated

import msgspec


class SortOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class PageOptions(msgspec.Struct):
    """
    Common pagination options for all endpoints implementing pagination of
    results.

    - page, for page number
    - limit, for results per page
    - continuation_id, the last numeric ID that was read
    """

    page: Annotated[int, msgspec.Meta(gt=0, description="Page number.")] = (
        msgspec.field(default=1)
    )  # type: ignore
    limit: Annotated[
        int,
        msgspec.Meta(gt=0, le=1000, description="Maximum number of results per page."),
    ] = msgspec.field(default=100)
    continuation_id: Annotated[
        int | None,
        msgspec.Meta(
            description="If provided, the ID of the last object that was retrieved.",
        ),
    ] = msgspec.field(default=None)
    sort_order: SortOrder = msgspec.field(default=SortOrder.ASC)


class TimedMixin(msgspec.Struct):
    created_at: datetime
    updated_at: datetime
    etag: str
