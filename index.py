import socket as sc
from sys import flags
import threading
from colorama import Fore
from scapy.all import *
from scapy.layers.inet import *

scan_TCP = sr1(IP(dst="10.0.0.107")/TCP(dport=[135], flags="S"))
# scan_UDP = sr1(IP(dst="10.0.0.35")/UDP(dport=[135]))
ttl_TCP = scan_TCP.getlayer(IP).ttl
# ttl_UDP = scan_UDP.getlayer(IP).ttl
print(ttl_TCP)
# print(ttl_TCP, ttl_UDP)
error = "système d'exploitation non détecté"

if ttl_TCP == 128:
    print(Fore.GREEN + "L'utilisateur utilise Windows")
if ttl_TCP == 64:
    print(Fore.GREEN + "L'utilisateur utilise Linux")
if ttl_TCP == 64:
    print(Fore.GREEN + "L'utilisateur utilise Mac")

'''
# détection par ports
ports = [135] # windows

# partie scan
def scan():
    for port in ports:
        submit = ("10.0.0.35")
        affichage = sc.gethostbyaddr(submit) # vérification avec le nom d'hôte si pc ne répond pas au ping
        print(f"démarrage du scan d'officience : {affichage}")
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        result = sock.connect_ex((submit, port))
        sc.setdefaulttimeout(0)
        print(affichage)
        windows_OS = ["LAPTOP-"]
        mac_OS = ["MACBOOKAIR-", "MacBook-"]
        android_OS = ["Android.", "Android-"]

        # vérification pour windows
        if result == 0 and ports[0] or affichage[0] in windows_OS:
            print(Fore.GREEN + f"utlisateur détecté sur le port : {port}")
            win = print("l'utilisateur utlise Windows")
            sock.close()

            # vérification pour mac
        if result == 0 or affichage[0] in mac_OS:
            mac = print(Fore.GREEN + "l'utilisateur utilise Mac")
            sock.close()
        else:
            print(Fore.RED + "utilisateur non détecté sur ce port")
            sock.close()

# partie accélération de scan
for i in range(1):
    thread = threading.Thread(target=scan).start()


'''
'''
# port[0] = "Windows"
# print(port[0])
# port[1] = "Mac"
# port[2::] = "Linux"
'''