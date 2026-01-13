from fastapi import FastAPI, APIRouter
import user
import recipe

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(recipe.router, prefix="/recipe", tags=["Recipe"])
