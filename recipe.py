from fastapi import FastAPI, HTTPException, APIRouter
from database_connector import get_connector
from models import Recipe, Unit, UpdateRecipe
from typing import List, Optional
from mysql.connector import Error

router = APIRouter()
# create a get all in which will retrieve all of the ingredients per recipe
