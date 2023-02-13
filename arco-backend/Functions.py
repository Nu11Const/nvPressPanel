from psutil import *
from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
app = FastAPI()
import json
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/api/index")
async def info():
    return {"status": "200","message":"欢迎进入nvPressPanel后端"}

@app.post("/api/get_performance")
async def get_performance():
    cpu = round(cpu_percent(interval=2))
    memory = round(virtual_memory()[2])
    response = {"status": "200","cpu":cpu,"memory": memory}
    return response

class LoginForm(BaseModel):
    username: str
    password: str

@app.post("/api/auth/login")
async def login(login:LoginForm):
    response = {"status":"200","message":"successful"}
    with open('config.json', 'r') as f:
        config = json.load(f)
        user = config["auth"]["username"]
        password = config["auth"]["password"]
        if(login.username != user or login.password != password):
            response["status"] = "403"
            response["message"] = "unauth"
        return response    
    
    
@app.get("/")
async def index(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})
