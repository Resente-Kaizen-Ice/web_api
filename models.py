from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Unit(str, Enum):
    litter = "litter"
    kilogram = "kilogram"
    cup = "cup"
    piece = "piece"


class Register(BaseModel):  # can be used to post and get
    first_name: str
    middle_name: Optional[str]
    last_name: str
    nickname: Optional[str]
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    nickname: Optional[str]
    email: Optional[str]
    password: Optional[str]


class Recipe(BaseModel):  # can be used to post and get
    recipe_name: str
    description: Optional[str]
    ingredient_name: str
    quantity: float
    unit: List[Unit]


class UpdateRecipe(BaseModel):
    recipe_name: Optional[str]
    description: Optional[str]
    ingredient_name: Optional[str]
    quantity: Optional[float]
    unit: Optional[List[Unit]]
