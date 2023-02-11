from flask import Flask, jsonify, redirect, render_template, request 
import json
from flask_cors import CORS, cross_origin
import os
from gevent import pywsgi
import threading
from psutil import *
app=Flask(__name__, static_url_path='')

@app.route('/api/list-files', methods=['GET'])
def test():
    gettoken = request.args.get('token','')
    if(open("password.txt", encoding='utf-8').read() ==  gettoken):
        return json.dumps(os.popen("ls").read())
    else:
         return redirect('/#/error/403')
    

@app.route('/api/get_auth',methods=['GET'])
def get_auth():
    getuser = request.args.get('user','')
    # password.txt是sha256加密数字
    getpassword = request.args.get('password','')
    password = open("password.txt", encoding='utf-8').read()
    user = open("user.txt", encoding='utf-8').read()
    if(getuser == user and getpassword == password):
        return json.dumps("true")
    else:
        return json.dumps("false")
    
@app.route("/api/get_performance",methods=['POST'])
def get_performance():
    cpu = cpu_percent(interval=2)
    memory = virtual_memory()[2]
    response = {"status": "200","cpu":cpu,"memory": memory}
    return jsonify(response)
    
@app.route('/api/run_nvpress_docker_container',methods=['GET'])
def run_nvpress_docker_container():
    gettoken = request.args.get('token','')
    if(open("password.txt", encoding='utf-8').read() ==  gettoken):
        os.system("mkdir -vp /www/nvpress/{themes,content,plugins}")
        response = os.popen("docker run -d -p 11111:8081 --name=nvPress --restart=always -v /www/nvpress/content:/usr/src/app/nv-content -v /www/nvpress/themes:/usr/src/app/nv-themes -v /www/nvpress/plugins:/usr/src/app/nv-plugins pandastd/nvpress:latest").read()
        return json.dumps(response)
    else:
         return redirect('/#/error/403')

@app.route('/api/restart_docker_service',methods=['GET'])
def restart_docker_service():
    gettoken = request.args.get('token','')
    if(open("password.txt", encoding='utf-8').read() ==  gettoken):
        return(json.dumps(os.popen("service docker restart").read()))
    else:
         return redirect('/#/error/403')
    

@app.route('/api/get_container_install_status',methods=['GET'])
def get_container_install_status():
    status = os.popen("docker ps").read()
    if("nvpress" not in status):
        return "false"
    elif("nvpress" in status):
        return "true"
    else:
        return "undefined"
    
@app.route('/api/get_caddyfile',methods=['GET'])
def get_caddyfile():
    caddyfile = open("/etc/caddy/Caddyfile", encoding='utf-8').read()
    return(json.dumps(caddyfile))

@app.route('/api/get_docker_daemon',methods=['GET'])
def get_docker_daemon():
    daemon = open("/etc/docker/daemon.json", encoding='utf-8').read()
    return(json.dumps(daemon))


filelist=[{
    'token' : '',
    'text' : ''
}   
]
@app.route("/api/uploadtext",methods=['GET','POST'])
def uploadtext_file():
        post_data = request.get_json()
        response_object = {'status': 'success'}
        if request.method == 'POST':
            filelist.append({
                'token': post_data.get('token'),
                'text': post_data.get('text')
            })
            filelist_dic = filelist[-1]
            if(filelist_dic['token'] == open("password.txt", encoding='utf-8').read()):
                with open("/etc/caddy/Caddyfile","w") as file:
                    file.write(filelist_dic['text'])
                os.system("sudo systemctl reload caddy")
            else:
                response_object['status'] = "403 unauth"
        else:
            response_object['data'] = filelist[-1]
        return jsonify(response_object)
    
    
@app.route("/api/uploadtext_docker",methods=['GET','POST'])
def uploadtext_file_docker():
        post_data = request.get_json()
        response_object = {'status': 'success'}
        if(post_data.get('token') == open("password.txt",encoding='utf-8').read()):
            with open("/etc/docker/daemon.json","w") as file:
                file.write(post_data.get('text'))
        else:
            response_object['status'] = "403 unauth"
        return jsonify(response_object)
    
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api/get_docker_status',methods=['GET'])
def get_docker_status():
    return json.dumps(os.popen("docker version").read())


if __name__ == '__main__':
    if(os.path.exists("pyftp.py") == True):
        import pyftp
        t1 = threading.Thread(target=pyftp.main, args=())
        t1.start()
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    cors = CORS(app)
    server.serve_forever()
