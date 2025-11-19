from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    recipes: List["Recipes"] = Relationship(
        back_populates="category",
        sa_relationship_kwargs={"cascade": "all, delete"}
    )

# Forward reference update
from APP.models.recipe import Recipes
Category.update_forward_refs()
