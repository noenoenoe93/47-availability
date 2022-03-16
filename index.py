import socket as sc
import threading
from colorama import Fore

ports = [135]
# partie scan
def scan():
    for port in ports:
        submit = ("10.0.0.17")
        affichage = sc.gethostbyaddr(submit)
        print(f"démarrage du scan d'officience : {affichage}")
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        result = sock.connect_ex((submit, port))
        sc.setdefaulttimeout(0)
        hostname = []
        hostname.append(hostname)
        print(hostname)
        '''
        if result == 0 and ports[0]:
            # print(Fore.GREEN + f"utlisateur détecté sur le port : {port}")
            win = print("l'utilisateur utlise Windows")
            sock.close()
            hostname.clear()
            '''
        if result == 0 and hostname in ("MAC"):
                mac = print("l'utilisateur utilise Mac")
                sock.close()
                hostname.clear()
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