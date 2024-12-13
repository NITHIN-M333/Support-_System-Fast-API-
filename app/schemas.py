from pydantic import BaseModel
from typing import List, Optional

class SupportPriceBase(BaseModel):
    amount: float
    name: str
    description: Optional[str]

class SupportPriceCreate(SupportPriceBase):
    pass

class SupportPrice(SupportPriceBase):
    id: int

    class Config:
        from_attributes = True


class SupportPurposeBase(BaseModel):
    name: str
    description: Optional[str]

class SupportPurposeCreate(SupportPurposeBase):
    pass

class SupportPurpose(SupportPurposeBase):
    id: int
    categories: List['SupportCategory'] = []

    class Config:
        from_attributes = True


class SupportCategoryBase(BaseModel):
    name: str
    description: Optional[str]
    active: bool = True

class SupportCategoryCreate(SupportCategoryBase):
    pass

class SupportCategory(SupportCategoryBase):
    id: int
    purposes: List[SupportPurpose] = []
    prices: List[SupportPrice] = []

    class Config:
        from_attributes = True

