from psutil import *
from fastapi import FastAPI, Cookie
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
import json
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")

@app.get("/api/index")
async def info():
    return {"status": "200","message":"欢迎进入nvPressPanel后端"}

class ChangeUsernameForm(BaseModel):
    newname: str

@app.post("/api/auth/change_username")
async def change_username(username:ChangeUsernameForm,token: Optional[str] = Cookie(None)):
    response = {"status":"200","message":"successful"}
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        fjtoken["auth"]["username"] = username.newname
        output = open("config.json","w")
        output.write(json.dumps(fjtoken))
        output.close()
    else:
        response["status"] = "403"
        response["message"] = "unauth"
    ftoken.close()
    return response
    
    


class ChangePasswordForm(BaseModel):
    oldpassword: str
    password: str

@app.post("/api/auth/change_password")
async def change_password(json_change:ChangePasswordForm):
    response = {"status":"200","message":"successful"}
    f = open('config.json', 'r')
    config = json.load(f)
    if(config["auth"]["password"] == json_change.oldpassword):
        config["auth"]["password"] = json_change.password
    else:
        response["status"] = "403"
        response["message"] = "unauth"
    output = open('config.json',"w")
    output.write(json.dumps(config))
    f.close()
    output.close()
    return response
        
    

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

print("Function函数加载完毕。")