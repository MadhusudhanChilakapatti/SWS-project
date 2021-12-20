import subprocess
import socket
import platform



def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s= socket.create_connection((host,80),2)
        s.close()
        print("Connected")
        return True
    except:
        print("No active internet connection")
        return False

def wifiname():
    my_os = platform.system()
    Remote_server = "1.1.1.1"
    if my_os == "Windows":
        print("windows")
        interface = subprocess.check_output(["netsh", "wlan", "show", "interface"])
        interface = interface.decode("ascii")
        if "disconnected" in interface:
            print("No active internet connection")
        else:
            network = subprocess.check_output(["netsh", "wlan", "show", "network"])
            network = network.decode("ascii")
            ls = network.split("\n")
            ls = ls[4:]
            ssids = []
            ssids.append(ls[0])
            ssid_name = ''.join(map(str,ssids))
            ssid_name = ssid_name[9:]
            check_for_connection = is_connected(Remote_server)
            return ssid_name
            #connect()
    elif my_os == "Linux":
        print("Linux")

get_stat = wifiname()
        




    

