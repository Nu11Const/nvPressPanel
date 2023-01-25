import os
import sys
def installdeps():
    os.environ.get('key_name')
    global result 
    result = input("\033[1m\033[32m[INPUT]\033[0m 请确认安装环境，国内/国外=y/n:")
    if (result == "y"):
        os.system("pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/")
    os.system("wget https://get.nvpress.tk/requirements.txt")
    os.system("sudo pip3 install -r ./requirements.txt")
    os.system("sudo mkdir -p /www/nvpresspanel")
    print("""
            ____                      ____                  _
 _ ____   _|  _ \ _ __ ___  ___ ___  |  _ \ __ _ _ __   ___| |
| '_ \ \ / / |_) | '__/ _ \/ __/ __| | |_) / _` | '_ \ / _ \ |
| | | \ V /|  __/| | |  __/\__ \__ \ |  __/ (_| | | | |  __/ |
|_| |_|\_/ |_|   |_|  \___||___/___/ |_|   \__,_|_| |_|\___|_|

          """)
    
def installDocker():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装Docker......")
    if(result == "y"):
        os.system("curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun")
        os.system("wget https://get.nvpress.tk/daemon.json -O /etc/docker/daemon.json")
        os.system("systemctl restart docker")
    else:
        os.system("curl -fsSL https://get.docker.com | bash")
    
def installVsftpd():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装FTP......")
    os.system("wget https://get.nvpress.tk/ftp.py -O /www/nvpresspanel/")
    
def generateCaddyfileAutoSSL(value1,value2):
    caddyfile =  value1+" {\n  reverse_proxy 127.0.0.1:11111\n  encode gzip\n  tls "+value2+"\n}"
    with open("/etc/caddy/Caddyfile","w") as file:
        file.write(caddyfile)     

def generateCaddyfile(value1,value2,value3):
    caddyfile = value1+" {\n reverse_proxy 127.0.0.1:11111\n encode gzip\n tls "+value2+" "+value3
    with open("/etc/caddy/Caddyfile","w") as file:
        file.write(caddyfile) 
    
def installCaddy():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装Caddy......")
    if(system == "debian"):
        os.system("sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https -y && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list && sudo apt update -y && sudo apt install caddy -y")
    elif (system == "redhat"):
        os.system("sudo yum install yum-plugin-copr -y && yum copr enable @caddy/caddy -y && yum install caddy -y")
    domain = input("\033[1m\033[32m[INPUT]\033[0m 请输入绑定域名:")
    ssl = input("\033[1m\033[32m[INPUT]\033[0m 请输入是否启用自动SSL,是/否=y/n:")
    if(ssl == "y"):
        autossl = True
        email = input("\033[1m\033[32m[INPUT]\033[0m 请输入绑定邮箱:")
        generateCaddyfileAutoSSL(domain,email)
        os.system("systemctl start caddy")
    else: 
        autossl = False
        cert = input("\033[1m\033[32m[INPUT]\033[0m 请输入域名证书:")
        key = input("\033[1m\033[32m[INPUT]\033[0m 请输入域名秘钥:")
        generateCaddyfile(domain,cert,key)
        os.system("systemctl start caddy")
        
        

def installPanel():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装面板主进程......")
    os.system("sudo wget -O panel.tar.gz https://get.nvpress.tk/panel.tar.gz")
    os.system("sudo tar -xvf  panel.tar.gz -C /www/nvpresspanel")
    os.system("sudo wget https://get.nvpress.tk/nvpress.service -O /etc/systemd/system/nvpress.service")
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl start nvpress")
    os.system("sudo systemctl enable nvpress")
    ip = os.popen("curl ip.sb").read()
    print("\033[1m\033[32m[INFO]\033[0m 安装完成！")
    print("打开:http://"+ip+":8080/ 访问面板")
    
     
if __name__=='__main__':
    global system 
    system = str(sys.argv[1])
    installdeps()
    installdockerresult = input("\033[1m\033[32m[INPUT]\033[0m 请确认是否已安装Docker,有/无=y/n:")
    if (installdockerresult == "n"):
        installDocker()
    else:pass
    installftpresult = input("\033[1m\033[32m[INPUT]\033[0m 请确认是否已安装FTP控件,有/无=y/n:")
    if(installftpresult == "n"):
        installVsftpd()
    else:pass
    installCaddy()
    installPanel()
    
