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
        return str(e)
def checkVulns(banner):
    # use external file as vlun banner source
    f = open("CH1_vuln_banners.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            return "[+] Server is vulnerable: " +\
            banner.strip('\n')
    else:
        return banner
def main():
    portList = [21,22,25,80,110,443]
    # use for iterate test of ports on one subnet
    for x in range(100,101):
        ip = '192.168.1.' + str(x)
        for port in portList:
            banner = retBanner(ip,port)
            if banner:
                print('[+] ' + ip + ':' + str(port) +
                      ' -> ' + checkVulns(banner))
if __name__ == '__main__':
    main()

# access objects maintained by the system
import sys
import os
filename = sys.argv[0]
filenum = len(sys.argv)
# check the file exists and accessible
if not os.path.isfile(filename):
    print('[-] ' + filename + ' does not exist.')
    exit(0)
if not os.access(filename, os.R_OK):
    print('[-] ' + filename + ' access denied.')
    exit(0)
print("[+] The number of arguments in current system is: " +
      str(filenum))
print("[+] Current Python script file is: " + filename)


