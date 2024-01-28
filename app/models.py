from pydantic import BaseModel, Field
from typing import List, Optional


class Costume(BaseModel):
    name: str
    medium: str
    gender: List[str]
    budget: str
    height: float
    glasses: Optional[str] = Field(None, description="Select whether you wear glasses or not.")
    hair: Optional[str] = Field(None, description="Select your hair length.")
    weight: float
    age: Optional[int] = Field(None, description="Enter your age.")

    props: List[str]
