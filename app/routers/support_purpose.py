from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database

router = APIRouter(prefix="/support-purpose", tags=["Support Purpose"])

@router.post("/", response_model=schemas.SupportPurpose)
def create_purpose(purpose: schemas.SupportPurposeCreate, db: Session = Depends(database.get_db)):
    return crud.create_support_purpose(db=db, support_purpose=purpose)

@router.get("/", response_model=List[schemas.SupportPurpose])
def read_purposes(db: Session = Depends(database.get_db)):
    return crud.get_support_purposes(db)
