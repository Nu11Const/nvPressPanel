from psutil import *
from fastapi import FastAPI, Cookie, HTTPException
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
from threading import Thread
import os
import subprocess
import sys
from typing import Optional
app = FastAPI()
import json
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")


## Written by new Bing ##
tasks = []
@app.post("/api/task/tasks")
async def get_tasks(token: Optional[str] = Cookie(None)):
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        return tasks
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()

def run_shell_command(command, task_id):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            tasks[task_id]["output"] += output.decode("utf-8")
    tasks[task_id]["status"] = "finished"
    tasks[task_id]["error"] = process.stderr.read().decode("utf-8")

@app.post("/api/task/do_job")
async def start_new_task(json_data: dict,token: Optional[str] = Cookie(None)):
    # Do something with the json data
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        task_id = len(tasks)
        tasks.append({"id": task_id, "status": "started", "output": ""})
        command = json_data["command"].split()
        thread = Thread(target=run_shell_command, args=(command, task_id))
        thread.start()
        return {"message": "New task started.", "task_id": task_id}
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()

@app.post("/api/task/get_job")
async def get_task_status(task_id: int,token: Optional[str] = Cookie(None)):
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        if task_id >= len(tasks):
            return {"message": "Invalid task ID."}
        return tasks[task_id]
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()
    
    
@app.post("/api/task/terminate_task")
def terminate_task(task_id: int,token: Optional[str] = Cookie(None)):
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        tasks[task_id]["status"] = "terminated"
        return "Task terminated."
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()
## Written by new Bing Finished ##


@app.post("/api/get_docker_installed")
async def get_docker_installed(token: Optional[str] = Cookie(None)):
    response = {"status": "200","message":"success","docker_installed": False}
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        if(os.path.exists("/usr/bin/docker")):
            response["docker_installed"] = True
        return response
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()




@app.post("/api/restart_server")
def restart(token: Optional[str] = Cookie(None)):
    response = {"status":"200","message":"successful"}
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()
    return response

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
        raise HTTPException(status_code=403, detail="unauth")
    ftoken.close()
    return response
    

class ChangePortForm(BaseModel):
    port: str

@app.post("/api/change_port")
async def change_port(port:ChangePortForm,token: Optional[str] = Cookie(None)):
    response = {"status":"200","message":"successful"}
    ftoken = open("config.json")
    fjtoken = json.load(ftoken)
    if(fjtoken["auth"]["password"] == token):
        fjtoken["port"] = port.port
        output = open("config.json","w")
        output.write(json.dumps(fjtoken))
        output.close
    else:
        raise HTTPException(status_code=403, detail="unauth")
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
        raise HTTPException(status_code=403, detail="unauth")
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
            raise HTTPException(status_code=403, detail="unauth")
        return response    
    
    
@app.get("/")
async def index(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})

print("Function函数加载完毕。")