import psutil
from time import sleep
import platform
from win32com.client import GetObject
from cpuinfo import cpuinfo
import socket
import shutil
import win32api
def memory_info():
    MEMORY = psutil.virtual_memory()
    MEMORY_USAGE = round((MEMORY.used / (1024 **3)),2)
    PROCENT_USAGE = MEMORY.percent 
    MEMORY_AVALIBLE = round((MEMORY.available/ (1024 **3)),2)
    return MEMORY_AVALIBLE, MEMORY_USAGE , PROCENT_USAGE
def procent_cpu_usage_averange_in_time(time):
    CPU_USAGE = []
    AVARANGE = 0
    for i in range(time):
        CPU_USAGE.append(float(psutil.cpu_percent(interval=1)))
    for i in CPU_USAGE:
        AVARANGE += i
    AVARANGE /= time
    del CPU_USAGE
    return AVARANGE
def get_cpu_name():#only for windows 
    root_winmgmts = GetObject("winmgmts:root\cimv2")
    cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
    return str(cpus[0].Name)
def get_cpu_name2():#linux osx system
    info= cpuinfo._get_cpu_info_from_sysinfo
    return info
def get_active_users():
    users = psutil.users()
    users2 =[]
    for i in range(len(users)):
            users2.append(users[i].name)
    return users2
def get_system_info():
    family = platform.system()
    system_name = platform.platform()
    system_version = platform.version()
    return family, system_name, system_version
def network_card_info():
    networkcard = []
    networkcardout = []
    for interface in sorted(psutil.net_if_addrs().keys()):
            ip_address = ""
            mac_address = ""
            for addr in psutil.net_if_addrs()[interface]:
                if addr.family == socket.AF_INET:
                    ip_address = addr.address
                if addr.family == psutil.AF_LINK:
                    mac_address = addr.address
            networkcard.append({"id": interface,
                            "ip_address": ip_address,
                            "mac_address": mac_address})
    for i in networkcard:
        networkcardout.append((i["id"],i['ip_address'],i['mac_address']))
    return networkcardout
def harddrive_usage():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    drives_usage = []
      
    for drives in drives:
        try:     
            usage = psutil.disk_usage(drives)
            drives_usage.append({'disk_letter': drives, 'total': usage[0]//(2**30), 'used': usage[1]//(2**30), 'free': usage[2]//(2**30)})
        except PermissionError:
            continue

    return drives_usage
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP






