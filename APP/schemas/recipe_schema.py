from sqlmodel import SQLModel

class RecipeCreate(SQLModel):
    name: str
    description: str | None = None
