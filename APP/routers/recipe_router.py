from fastapi import APIRouter,Depends
from sqlmodel import Session
from APP.database import get_session
from APP.models.recipe import Recipes
from APP.crud.recipe_crud import create_recipe,get_recipe,update_recipe,delete_recipe_byID,get_recipe_byID

router=APIRouter(prefix="/recipes",tags=["recipes"])

@router.post('/')
def add_recipe(recipe:Recipes,db:Session=Depends(get_session)):
    return create_recipe(db,recipe)

@router.get('/')
def get_all(db:Session=Depends(get_session)):
    return get_recipe(db)

@router.get('/{findID}')
def get_By_id(findID:int,db:Session=Depends(get_session)):
    return get_recipe_byID(db,findID)

@router.put('/{upd_ID}')
def update_single_recipe(upd_ID: int, recipe: Recipes, db: Session = Depends(get_session)):
    return update_recipe(db, upd_ID, recipe)

@router.delete('/{delId}')
def delete_recipe(delId:int,db:Session=Depends(get_session)):
    return delete_recipe_byID(db,delId)