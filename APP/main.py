from fastapi import FastAPI
from APP.database import create_db_tables,create_engine,test_connection
from APP.routers.recipe_router import router
from APP.routers.category_router import router as category_router

app=FastAPI()

create_db_tables()
app.include_router(router)
app.include_router(category_router)

@app.get("/")
def home():
    db = test_connection()
    if db:
        return {"message": "Database connected successfully"}
    else:
        return {"message": "Failed to connect to the database"}

