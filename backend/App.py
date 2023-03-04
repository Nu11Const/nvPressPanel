import uvicorn
import json
if __name__ == '__main__':
    print("""
            ____                    ____                  _ 
 _ ____   _|  _ \ _ __ ___  ___ ___|  _ \ __ _ _ __   ___| |
| '_ \ \ / / |_) | '__/ _ \/ __/ __| |_) / _` | '_ \ / _ \ |
| | | \ V /|  __/| | |  __/\__ \__ \  __/ (_| | | | |  __/ |
|_| |_|\_/ |_|   |_|  \___||___/___/_|   \__,_|_| |_|\___|_|

          """)
    port = open("config.json")
    port_num = json.load(port)
    uvicorn.run(app='Functions:app', host='127.0.0.1', port=int(port_num["port"]), reload=True)
    port.close()