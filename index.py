import socket as sc
import threading
from colorama import Fore
from scapy.all import *
from scapy.layers.inet import *

# détection par ports
ports = [135] # windows
win = Fore.GREEN + "l'utilisateur utlise Windows"
mac = Fore.GREEN + "l'utilisateur utilise Mac"
linux = Fore.GREEN + "l'utilisateur utilise linux"
android = Fore.GREEN + "l'utilisateur utilise android"

# partie scan
def scan():
    for port in ports:
        # partie détection 1
        submit = ("192.168.0.1")
        affichage = sc.gethostbyaddr(submit) # vérification avec le nom d'hôte si pc ne répond pas au ping
        print(f"démarrage du scan d'officience : {affichage}")
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        result = sock.connect_ex((submit, port))
        sc.setdefaulttimeout(0)
        print(affichage)
        windows_OS = ["LAPTOP-"]
        mac_OS = ["MACBOOKAIR-", "MacBook-"]
        android_OS = ["Android.", "Android-"]
        linux_OS = ["LINUX"]

        # partie vérification windows
        if result == 0 and ports[0] and affichage[0] in windows_OS:
            print(Fore.GREEN + f"utlisateur détecté sur le port : {port}")
            print(win)
            sock.close()

        # vérification pour mac
        if result == 0 and affichage[0] in mac_OS:
            print(mac)
            sock.close()

        # vérification pour linux
        if result == 0 and affichage[0] in linux_OS:
            print(linux)
            sock.close()

        # vérification pour android
        if result == 0 and affichage[0] in android_OS:
            print(android)
            sock.close()
        
        elif result == 1:
            sock.close()
            scan2()

def scan2(): 
    # partie détection 2 si 1 ne marche pas
    scan_TCP = sr1(IP(dst="192.168.0.1")/TCP(dport=[135], flags="S"))
    scan_UDP = sr1(IP(dst="192.168.0.1")/UDP(dport=[67]))
    scan_ICMP = sr1(IP(dst="192.168.0.1")/ICMP())
    ttl_TCP = scan_TCP.getlayer(IP).ttl
    ttl_UDP = scan_UDP.getlayer(IP).ttl
    ttl_ICMP = scan_ICMP.getlayer(IP).ttl
    print(ttl_TCP, ttl_UDP, ttl_ICMP)

    if ttl_TCP == 128 or ttl_UDP == 128 or ttl_ICMP == 128:
        print(win)

    if ttl_TCP == 64 or ttl_UDP == 64 or ttl_ICMP == 64:
        print(mac)

# partie accélération de scan
for i in range(1):
    thread = threading.Thread(target=scan).start()
    thread = threading.Thread(target=scan2).start()

'''
# port[0] = "Windows"
# print(port[0])
# port[1] = "Mac"
# port[2::] = "Linux"
'''