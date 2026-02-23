from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.endpoints import router as api_router

app = FastAPI(title="Ma Super App FastAPI")

# On configure l'accès aux templates
templates = Jinja2Templates(directory="templates")

app.include_router(api_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # On renvoie le fichier index.html
    return templates.TemplateResponse("index.html", {"request": request})