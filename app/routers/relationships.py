from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database, schemas

router = APIRouter(prefix="/relationships", tags=["Relationships"])


# Associate a category with a purpose
@router.post("/assign-category-to-purpose/")
def assign_category_to_purpose(
    purpose_name: str, category_name: str, db: Session = Depends(database.get_db)
):
    purpose = db.query(models.SupportPurpose).filter(models.SupportPurpose.name == purpose_name).first()
    category = db.query(models.SupportCategory).filter(models.SupportCategory.name == category_name).first()

    if not purpose:
        raise HTTPException(status_code=404, detail="SupportPurpose not found")
    if not category:
        raise HTTPException(status_code=404, detail="SupportCategory not found")

    if category in purpose.categories:
        raise HTTPException(status_code=400, detail="Category already assigned to Purpose")

    purpose.categories.append(category)
    db.commit()
    return {"message": f"Category '{category_name}' assigned to Purpose '{purpose_name}' successfully"}


# Associate a price with a category
@router.post("/assign-price-to-category/")
def assign_price_to_category(
    category_name: str, price_name: str, db: Session = Depends(database.get_db)
):
    category = db.query(models.SupportCategory).filter(models.SupportCategory.name == category_name).first()
    price = db.query(models.SupportPrice).filter(models.SupportPrice.name == price_name).first()

    if not category:
        raise HTTPException(status_code=404, detail="SupportCategory not found")
    if not price:
        raise HTTPException(status_code=404, detail="SupportPrice not found")

    if price in category.prices:
        raise HTTPException(status_code=400, detail="Price already assigned to Category")

    category.prices.append(price)
    db.commit()
    return {"message": f"Price '{price_name}' assigned to Category '{category_name}' successfully"}


# Get all categories for a purpose
@router.get("/categories-for-purpose/{purpose_name}", response_model=schemas.SupportPurpose)
def get_categories_for_purpose(purpose_name: str, db: Session = Depends(database.get_db)):
    purpose = db.query(models.SupportPurpose).filter(models.SupportPurpose.name == purpose_name).first()

    if not purpose:
        raise HTTPException(status_code=404, detail="SupportPurpose not found")

    return purpose


# Get all prices for a category
@router.get("/prices-for-category/{category_name}", response_model=schemas.SupportCategory)
def get_prices_for_category(category_name: str, db: Session = Depends(database.get_db)):
    category = db.query(models.SupportCategory).filter(models.SupportCategory.name == category_name).first()

    if not category:
        raise HTTPException(status_code=404, detail="SupportCategory not found")

    return category


# Get all purposes for a category
@router.get("/purposes-for-category/{category_name}", response_model=schemas.SupportCategory)
def get_purposes_for_category(category_name: str, db: Session = Depends(database.get_db)):
    category = db.query(models.SupportCategory).filter(models.SupportCategory.name == category_name).first()

    if not category:
        raise HTTPException(status_code=404, detail="SupportCategory not found")

    return category
