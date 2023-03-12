import subprocess
from fastapi import FastAPI
from threading import Thread
## Programed by New Bing
app = FastAPI()

tasks = []
@app.post("/task/tasks")
async def get_tasks():
    return tasks

def run_shell_command(command, task_id):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            tasks[task_id]["output"] += output.decode("utf-8")
        if tasks[task_id]["status"] == "terminated":
            tasks[task_id]["error"] = "Task terminated by user."
            break
    tasks[task_id]["status"] = "finished"
    tasks[task_id]["error"] = process.stderr.read().decode("utf-8")

@app.post("/task/terminate_task")
def terminate_task(task_id: int):
    tasks[task_id]["status"] = "terminated"
    return "Task terminated."

@app.post("/task/do_command")
async def start_new_task(json_data: dict):
    # Do something with the json data
    print(json_data)
    task_id = len(tasks)
    tasks.append({"id": task_id, "status": "started", "output": ""})
    command = json_data["command"].split()
    thread = Thread(target=run_shell_command, args=(command, task_id))
    thread.start()
    return {"message": "New task started.", "task_id": task_id}

@app.post("/task/get_job")
async def get_task_status(task_id: int):
    if task_id >= len(tasks):
        return {"message": "Invalid task ID."}
    return tasks[task_id]