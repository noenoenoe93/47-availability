import socket as sc
import threading
from colorama import Fore
from scapy.all import *
from scapy.layers.inet import *

# variables d'affichage OS
win = Fore.GREEN + "l'utilisateur utlise Windows"
linux = Fore.GREEN + "l'utilisateur utilise linux"
mac = Fore.GREEN + "l'utilisateur utilise Mac"
android = Fore.GREEN + "l'utilisateur utilise android"

# partie scan
def scan():
        # partie détection 1
        port = 1
        submit = ("10.0.0.8")
        affichage = sc.gethostbyaddr(submit)
        print(f"démarrage du scan d'officience : {affichage}")
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        result = sock.connect_ex((submit, port))
        sc.setdefaulttimeout(0)
        print(affichage)
        windows_OS = ["LAPTOP-"]
        mac_OS = ["MACBOOKAIR-", "MacBook-", "MACBOOKPRO-"]
        android_OS = ["Android.", "Android-"]
        linux_OS = ["LINUX"]

        # partie vérification windows
        for x in windows_OS[0::]:
            if x in affichage[0]:
                print(win)
                sock.close()

            elif result == 1:
                sock.close()
        
        # vérification pour mac
        for z in mac_OS[0::]:
            if z in affichage[0]:
                print(mac)
                sock.close()

            elif result == 1:
                sock.close()

        # vérification pour linux
        for s in linux_OS[0::]:
            if s in affichage[0]:
                print(linux)
                sock.close()
            
            elif result == 1:
                sock.close()

        # vérification pour android
        for l in android_OS[0::]:
            if l in affichage[0]:
                print(android)
                sock.close()
            
            elif result == 1:
                sock.close()
                exit()

'''       
def scan2(): 
    # partie détection 2 si 1 ne marche pas
    scan_TCP = sr1(IP(dst="10.0.0.35")/TCP(dport=[135], flags="S"))
    scan_UDP = sr1(IP(dst="10.0.0.35")/UDP(dport=[67]))
    scan_ICMP = sr1(IP(dst="10.0.0.35")/ICMP())
    ttl_TCP = scan_TCP.getlayer(IP).ttl
    ttl_UDP = scan_UDP.getlayer(IP).ttl
    ttl_ICMP = scan_ICMP.getlayer(IP).ttl
    print(ttl_TCP, ttl_UDP, ttl_ICMP)

    if ttl_TCP == 128 or ttl_UDP == 128 or ttl_ICMP == 128:
        print(win)

    if ttl_TCP == 64 or ttl_UDP == 64 or ttl_ICMP == 64:
        print(mac)
'''
# partie accélération de scan
for i in range(1):
    thread = threading.Thread(target=scan).start()
    # thread = threading.Thread(target=scan2).start()


'''
# port[0] = "Windows"
# print(port[0])
# port[1] = "Mac"
# port[2::] = "Linux"
'''