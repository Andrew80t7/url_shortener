from datetime import datetime
from pydantic import BaseModel, HttpUrl


class UrlBase(BaseModel):
    original_url: HttpUrl


class UrlCreate(UrlBase):
    pass


class UrlRead(UrlBase):
    short_key: str
    created_at: datetime
    user_id: int


    class Config:
        from_attributes = True


        