from threading import Thread
import socket
import select
from client import Client


class Receiver(Thread):

    def __init__(self, clients_list):
        Thread.__init__(self)
        self.clients_list = clients_list

    def run(self):

        hote = ''
        port = 5053

        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((hote, port))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port \"{}\".".format(port))

        clients_connectes = []

        while True:

            connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)

            for connexion in connexions_demandees:
                connexion_avec_client, infos_connexion = connexion.accept()
                clients_connectes.append(connexion_avec_client)

            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
            except select.error:
                pass

            else:
                for client in clients_a_lire:
                    received = client.recv(1024)
                    received = received.decode()
                    client_object = Client(received, client)
                    is_object_already_contained = False

                    for clients_objects in self.clients_list:
                        if clients_objects.get_public_IP() == client_object.get_public_IP() and clients_objects.get_local_IP() == client_object.get_local_IP():
                            is_object_already_contained = True
                            clients_objects.set_last_message(received.split(",")[4])

                    if not is_object_already_contained:
                        self.clients_list.append(client_object)
                        output_message = "Nouveau client > " + client_object.get_last_message()
                    else:
                        output_message = client_object.get_username() + " > " + client_object.get_last_message()

                    print(output_message)