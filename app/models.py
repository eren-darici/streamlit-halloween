from pydantic import BaseModel, Field
from typing import List, Optional


class Costume(BaseModel):
    name: str
    medium: str
    gender: List[str]
    budget: str
    height_feet: int
    height_inches: int
    glasses: Optional[str] = Field(description="Select whether you wear glasses or not. Yes if you are wearing, No if you are not.")
    hair: Optional[str] = Field(description="Select your hair length.")
    ethnicity: Optional[str]
    weight: float
    age: Optional[int] = Field(description="Enter your age. It should be an integer")

    props: List[str]
