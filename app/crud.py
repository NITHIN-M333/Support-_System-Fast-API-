from sqlalchemy.orm import Session 
from app import models, schemas
from fastapi import HTTPException

# CRUD operations for SupportPrice
def create_support_price(db: Session, support_price: schemas.SupportPriceCreate):
    db_price = models.SupportPrice(**support_price.model_dump())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

def get_support_prices(db: Session):
    return db.query(models.SupportPrice).all()

# Update a SupportPrice
def update_support_price(db: Session, price_id: int, support_price: schemas.SupportPriceBase):
    db_price = db.query(models.SupportPrice).filter(models.SupportPrice.id == price_id).first()
    if not db_price:
        raise HTTPException(status_code=404, detail="SupportPrice not found")

    for key, value in support_price.model_dump().items():
        setattr(db_price, key, value)

    db.commit()
    db.refresh(db_price)
    return db_price

# Delete a SupportPrice
def delete_support_price(db: Session, price_id: int):
    db_price = db.query(models.SupportPrice).filter(models.SupportPrice.id == price_id).first()
    if not db_price:
        raise HTTPException(status_code=404, detail="SupportPrice not found")

    db.delete(db_price)
    db.commit()
    return {"message": "SupportPrice deleted successfully"}


# CRUD operations for SupportPurpose
def create_support_purpose(db: Session, support_purpose: schemas.SupportPurposeCreate):
    db_purpose = models.SupportPurpose(**support_purpose.model_dump())
    db.add(db_purpose)
    db.commit()
    db.refresh(db_purpose)
    return db_purpose

def get_support_purposes(db: Session):
    return db.query(models.SupportPurpose).all()

# CRUD operations for SupportCategory
def create_support_category(db: Session, support_category: schemas.SupportCategoryCreate):
    db_category = models.SupportCategory(**support_category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_support_categories(db: Session):
    return db.query(models.SupportCategory).all()