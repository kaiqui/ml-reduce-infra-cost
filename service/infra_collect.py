import psutil
import socket
import requests
import time

 
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
def system_info():
    return dict(
        local_ip=get_local_ip(),
        hostname=socket.gethostname(),
        cpu_percent=psutil.cpu_percent(interval=1),
        cpu_core=psutil.cpu_count(),
        cpu_load=round(psutil.getloadavg()[1],2),
        virtual_memory=psutil.virtual_memory().percent,
        swap_memory=psutil.swap_memory().percent,
        disk_usage=psutil.disk_usage('/').percent
    )

while True:
    r = requests.post(url='http://localhost:8080', verify=False, data=system_info())
    print(r.text)
    time.sleep(60*5)