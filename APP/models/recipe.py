from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Recipes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None

    category_id: int | None = Field(default=None, foreign_key="category.id")
    category: Optional["Category"] = Relationship(back_populates="recipes")

# Forward reference update
from APP.models.category import Category
Recipes.update_forward_refs()
