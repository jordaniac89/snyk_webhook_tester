from __future__ import annotations

from pydantic import BaseModel


class Org(BaseModel):
    name: str
    id: str
    slug: str
    url: str
    created: str