from threading import Thread
import socket
import time


class Receiver(Thread):

    def __init__(self, clients_list):
        Thread.__init__(self)
        self.clients_list = clients_list

    def does_clients_list_contains(self, client):
        for clients_objects in self.clients_list:
            if clients_objects.is_same_client(client):
                return True
        return False

    def run(self):

        hote = ""
        port = 5053

        connection_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_to_server.connect((hote, port))
        print("Connexion établie avec le serveur sur le port \"{}\".".format(port))

        while True:
            received_msg = connection_to_server.recv(1024)
            print(received_msg.decode())
            time.sleep(1)