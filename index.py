import socket as sc
import threading
from colorama import Fore
from mac_vendor_lookup import MacLookup

# détection par ports
ports = [135] # windows

# partie scan
def scan():
    for port in ports:
        submit = ("192.168.0.29")
        affichage = sc.gethostbyaddr(submit) # vérification avec le nom d'hôte si pc ne répond pas au ping
        print(f"démarrage du scan d'officience : {affichage}")
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        result = sock.connect_ex((submit, port))
        sc.setdefaulttimeout(0)
        print(affichage)
        windows_PC = ["DELL", "DESKTOP", "COMPUTER", "nono", "Intel Corporate"]
        mac_PC = ["MAC"]

        # vérification pour windows
        if result == 0 and ports[0] or affichage[0] in windows_PC or MacLookup().lookup(submit) in windows_PC:
            print(Fore.GREEN + f"utlisateur détecté sur le port : {port}")
            win = print("l'utilisateur utlise Windows")
            sock.close()

            # vérification pour mac
        if result == 0 or affichage[0] in mac_PC:
            mac = print(Fore.GREEN + "l'utilisateur utilise Mac")
            sock.close()
        else:
            print(Fore.RED + "utilisateur non détecté sur ce port")
            sock.close()

# partie accélération de scan
for i in range(1):
    thread = threading.Thread(target=scan).start()


'''
# port[0] = "Windows"
# print(port[0])
# port[1] = "Mac"
# port[2::] = "Linux"
'''