from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from typing import List

router = APIRouter(prefix="/support-price", tags=["Support Price"])

@router.post("/", response_model=schemas.SupportPrice)
def create_price(price: schemas.SupportPriceCreate, db: Session = Depends(database.get_db)):
    return crud.create_support_price(db=db, support_price=price)

@router.get("/", response_model=List[schemas.SupportPrice])
def read_prices(db: Session = Depends(database.get_db)):
    return crud.get_support_prices(db)

@router.put("/{price_id}", response_model=schemas.SupportPrice)
def update_price(price_id: int, price: schemas.SupportPriceBase, db: Session = Depends(database.get_db)):
    return crud.update_support_price(db=db, price_id=price_id, support_price=price)

@router.delete("/{price_id}")
def delete_price(price_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_support_price(db=db, price_id=price_id)
