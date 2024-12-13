from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database

router = APIRouter(prefix="/support-category", tags=["Support Category"])

@router.post("/", response_model=schemas.SupportCategory)
def create_category(category: schemas.SupportCategoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_support_category(db=db, support_category=category)

@router.get("/", response_model=List[schemas.SupportCategory])
def read_categories(db: Session = Depends(database.get_db)):
    return crud.get_support_categories(db)
