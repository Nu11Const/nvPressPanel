import os
import sys
def installdeps():
    os.environ.get('key_name')
    global result 
    result = input("\033[1m\033[32m[INPUT]\033[0m 请确认安装环境，国内/国外=y/n:")
    if (result == "y"):
        os.system("pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/")
    os.system("wget https://get.nvpress.tk/requirements.txt")
    os.system("pip3 install -r ./requirements.txt")
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
    else:
        os.system("curl -fsSL https://get.docker.com | bash")
    
def installVsftpd():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装Vsftpd......")
    if(system == "debian"):
        os.system("sudo apt install vsftpd -y")
    if(system == "redhat"):
        os.system("sudo yum install vsftpd -y")
    
def installCaddy():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装Caddy......")
    if(system == "debian"):
        os.system("sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https -y && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list && sudo apt update -y && sudo apt install caddy -y")
    elif (system == "redhat"):
        os.system("sudo yum install yum-plugin-copr -y && yum copr enable @caddy/caddy -y && yum install caddy -y")

def installPanel():
    print("\033[1m\033[32m[INFO]\033[0m 正在启动安装面板主进程......")
    os.system("wget -O panel.zip https://get.nvpress.tk/panel.zip")
    
     
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
    