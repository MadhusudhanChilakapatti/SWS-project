import urllib.request
import subprocess

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        print("connected")
    except:
        print("No active internet connection")

        
results1 = subprocess.check_output(["netsh", "wlan", "show", "interface"])
print(results1)
results1 = results1.decode("ascii")
print(results1)
print(results1)
if "disconnected" in results1:
    print("No active internet connection")
else:
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    ssids.append(ls[0])
    mystr = ''.join(map(str,ssids))
    mystr1 = mystr[9:]
    print(mystr1)
    connect()




    

