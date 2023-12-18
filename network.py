import binascii
import ipaddress as ipa
from socket import *

# Addresses = ['10.10.20.113',
#              'fe80::5b92:b3c:280e:c6f5',]
#
# for ipaddr in Addresses:
#     addr = ipa.ip_address(ipaddr)
#     print(f"IP address: {addr!r}")
#     print("IP version : ", addr.version)
#     print("Packed addr: ", binascii.hexlify(addr.packed))
#     print("Interger addr : ", int(addr))
#     print("Is private? : ", addr.is_private)
#     print()

# print(socket.gethostname())
#
# HOSTS = ["www.uou.ac.kr",
#         "www.dongyang.ac.kr",
#         "www.python.org",
#         "testname",
#         "iot-System-Product-Name",
#         "www.naver.com",]

# for host in HOSTS:
#     try:
#         print('{} : {}'.format(host, socket.gethostbyname(host)))
#     except socket.error as e_msg:
#         print('{} : {}'.format(host, e_msg))
#
# for host in HOSTS:
#     print(host)
#     try:
#         hostname, aliases, addresses = socket.gethostbyname_ex(host)
#         print('hostname : ', hostname)
#         print('aliases : ', aliases)
#         print('addresses : ', addresses)
#     except socket.error as emsg:
#         print('ERROR:', emsg)


# hostname, aliaslist, ipaddrlist = gethostbyaddr('203.249.39.46')

# print('Hostname :', hostname)
# print('Aliases :', aliaslist)
# print('Addresses :', ipaddrlist)

print(getservbyname('telnet'))
print(getservbyport(80))