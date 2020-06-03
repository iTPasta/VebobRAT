import socket
import getpass
from requests import get

hote = ""
port = 5053

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    public_IP = get('https://api.ipify.org').text
    local_IP = socket.gethostbyname(socket.gethostname())
    username = getpass.getuser()
    network_username = socket.gethostname()
    msg_a_envoyer = public_IP + "," + local_IP + "," + username + "," + network_username + "," + input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer)

print("Fermeture de la connexion")
connexion_avec_serveur.close()