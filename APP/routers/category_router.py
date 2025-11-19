from fastapi import APIRouter, Depends
from sqlmodel import Session
from APP.database import get_session
from APP.models.category import Category
from APP.crud.category_crud import (
    create_category, get_categories, get_category_by_id, delete_category, update_category
)

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/")
def add_category(category: Category, db: Session = Depends(get_session)):
    return create_category(db, category)

@router.get("/")
def get_all_categories(db: Session = Depends(get_session)):
    return get_categories(db)

@router.get("/{cat_id}")
def get_single_category(cat_id: int, db: Session = Depends(get_session)):
    return get_category_by_id(db, cat_id)

@router.delete("/{cat_id}")
def remove_category(cat_id: int, db: Session = Depends(get_session)):
    return delete_category(db, cat_id)

@router.put("/{cat_id}")
def update_single_category(cat_id: int, category: Category, db: Session = Depends(get_session)):
    return update_category(db, cat_id, category)
