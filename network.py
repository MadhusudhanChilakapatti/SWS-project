import subprocess
import socket
global platform


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
    print("Platform: \n 1.Windows \n 2.Linux \n ")
    platform = int(input())
    Remote_server = "1.1.1.1"
    if platform == 1:
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
    elif platform == 2:
        print("Linux")

get_stat = wifiname()
        




    

