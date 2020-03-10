import configparser
import scan
import time
import socket

Config = configparser.ConfigParser()
Config.read("agent.ini")
ServerIP=Config.get('ConnectionSettings','IP')
SererPort = Config.get('ConnectionSettings','Port')
TimeConnection=Config.get('ConnectionSettings','Time')

myHostname= socket.gethostname()
myIP= scan.get_ip()

