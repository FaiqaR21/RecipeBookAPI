from sqlmodel import Session, select
from APP.models.category import Category
from fastapi import HTTPException

def create_category(db: Session, category: Category):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.exec(select(Category)).all()

def get_category_by_id(db: Session, cat_id: int):
    category = db.exec(select(Category).where(Category.id == cat_id)).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category 

def delete_category(db: Session, cat_id: int):
    category = get_category_by_id(db, cat_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category & its recipes deleted"}

def update_category(db: Session, cat_id: int, category_data: Category):
    category = get_category_by_id(db, cat_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.name = category_data.name or category.name
    db.commit()
    db.refresh(category)
    return category
