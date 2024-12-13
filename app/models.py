from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

purpose_category_table = Table(
    'purpose_category',
    Base.metadata,
    Column('purpose_id', Integer, ForeignKey('support_purpose.id')),
    Column('category_id', Integer, ForeignKey('support_category.id'))
)

category_price_table = Table(
    'category_price',
    Base.metadata,
    Column('category_id', Integer, ForeignKey('support_category.id')),
    Column('price_id', Integer, ForeignKey('support_price.id'))
)

class SupportPrice(Base):
    __tablename__ = 'support_price'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    categories = relationship("SupportCategory",secondary=category_price_table, back_populates="prices")

class SupportPurpose(Base):
    __tablename__ = 'support_purpose'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    categories = relationship("SupportCategory", secondary=purpose_category_table, back_populates="purposes")

class SupportCategory(Base):
    __tablename__ = 'support_category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    active = Column(Boolean, default=True)
    purposes = relationship("SupportPurpose", secondary=purpose_category_table, back_populates="categories")
    prices = relationship("SupportPrice", secondary=category_price_table, back_populates="categories")
