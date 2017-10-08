# some comment goes after #
print ("Hello World")

# variables
port = 21
banner = "FreeFloat FTP Server"
print ("[+] Checking for " + banner +
       " on port " + str(port))

# types of variables are set automatically
portList = [21,22,80,110]
portOpen = True
print(type(port))
print(type(banner))
print(type(portList))
print(type(portOpen))

# string variable has useful methods
print(banner)
print(banner.upper())
print(banner.lower())
print(banner.replace('FreeFloat','Ability'))
print(banner.find('FTP'))

# list variable has append, sort, and other methods
portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
print(portList)
portList.sort()
print(portList)
pos = portList.index(80)
print("[+] There are " + str(pos) +
      " ports to scan before 80.")
portList.remove(443)
print(portList)
cnt = len(portList)
print("[+] Scanning " + str(cnt) +
      " Total Ports.")

# dictionaries
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
print(services.keys())
print(services.items())
# has_key is removed in Python 3
# services.has_key('ftp') does not work
print('ftp' in services)
print(services['ftp'])
print("[+] Found vuln with FTP on port " + str(services['ftp']))

# networking method from socket module
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
# enhanced with exception handling
try:
    s.connect(("192.168.1.121",21))
    ans = s.recv(1024)
    print(ans)
except Exception as e:
    print("[-] Error = " + str(e))

# use function to perform the task above
import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return "Error -> " + str(e)
def checkVulns(banner):
    if '[WinError 10061]' in banner:
        return "Error -> request refused"
    else:
        return banner
def main():
    ip1 = "192.168.1.1"
    ip2 = "192.168.1.120"
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print('[+] ' + ip1 + ': ' + checkVulns(banner1))
    banner2 = retBanner(ip2, port)
    if banner2:
        print('[+] ' + ip2 + ': ' + checkVulns(banner2))
if __name__ == '__main__':
    main()

