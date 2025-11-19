from sqlmodel import Session,select
from APP.database import get_session
from APP.models.recipe import Recipes
from fastapi import HTTPException

def create_recipe(db: Session, recipe: Recipes):
    if recipe.category_id:
        from APP.crud.category_crud import get_category_by_id
        get_category_by_id(db, recipe.category_id)  # validate category
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


def get_recipe(db:Session):
    rec= db.exec(select(Recipes)).all()
    if rec:
        return rec
    else:
        raise HTTPException(status_code=404,detail="Recipe not found")

def get_recipe_byID(db:Session,findID:int):
    recipe=db.get(Recipes,findID)
    if recipe:
        return recipe
    else:
        raise HTTPException(status_code=404,detail="Invalid!!Recipe not found")

def update_recipe(db:Session,upd_ID:int,recipe_data):
    recipe=db.get(Recipes,upd_ID)
    if not recipe :
        raise HTTPException(status_code=404,detail="Recipe not Found")
    else:
        recipe.name = recipe_data.name or recipe.name
        recipe.description = recipe_data.description or recipe.description
        db.commit()
        db.refresh(recipe)
        return recipe
    
def delete_recipe_byID(db:Session,delId:int):
    recipe=db.get(Recipes,delId)
    if not recipe :
        raise HTTPException(status_code=404,detail="Recipe not Found")
    else:
        db.delete(recipe)
        db.commit()
        return {"message": "Recipe deleted successfully"}
