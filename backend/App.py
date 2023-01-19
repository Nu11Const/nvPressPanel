from flask import Flask, render_template, request 
import json
from flask_cors import CORS, cross_origin
import os
from gevent import pywsgi
app=Flask(__name__, static_url_path='')

@app.route('/api/list-files', methods=['GET'])
def test():
    return json.dumps(os.popen("ls").read())

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
@app.route('/api/run_nvpress_docker_container',methods=['GET'])
def run_nvpress_docker_container():
    os.system("mkdir -vp /www/nvpress/{themes,content,plugins}")
    os.system("docker run -d -p 8888:8081 --name=nvPress --restart=always -v /www/nvpress/content:/usr/src/app/nv-content -v /www/nvpress/themes:/usr/src/app/nv-themes -v /www/nvpress/plugins:/usr/src/app/nv-plugins pandastd/nvpress:latest")
    return "true"

@app.route('/api/restart_docker_service',methods=['GET'])
def restart_docker_service():
    return(json.dumps(os.popen("service docker restart").read()))

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

@app.route("/api/uploadtext",methods=['GET'])
def uploadtext_file():
    gettext = request.args.get('text','')
    with open("/etc/caddy/Caddyfile", 'w') as file_object:
        file_object.write(gettext)
    return "200 successful"
    
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api/get_docker_status',methods=['GET'])
def get_docker_status():
    return json.dumps(os.popen("docker version").read())

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    cors = CORS(app)
    server.serve_forever()
