from threading import Thread
import socket
import select
import time

from server.client import Client


class Receiver(Thread):

    def __init__(self, clients_list):
        Thread.__init__(self)
        self.clients_list = clients_list

    def does_clients_list_contains(self, client):
        for clients_objects in self.clients_list:
            if clients_objects.is_same_client(client):
                return True
        return False

    def get_same_client(self, client):
        for clients_objects in self.clients_list:
            if clients_objects.is_same_client(client):
                return clients_objects
        return

    def run(self):

        hote = ''
        port = 5053

        main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_connection.bind((hote, port))
        main_connection.listen(5)
        print("Le serveur écoute à présent sur le port \"{}\".".format(port))

        connected_clients = []

        while True:

            asked_connections, wlist, xlist = select.select([main_connection], [], [], 0.05)

            for connection in asked_connections:
                connection_with_client, infos_connection = connection.accept()
                connected_clients.append(connection_with_client)

            clients_to_read = []

            try:
                clients_to_read, wlist, xlist = select.select(connected_clients, [], [], 0.05)
            except select.error:
                pass

            else:
                for client in clients_to_read:
                    received = client.recv(1024)
                    received = received.decode()
                    client_object = Client(received, client)

                    if not self.does_clients_list_contains(client_object):
                        self.clients_list.append(client_object)
                        output_message = "Nouveau client > " + client_object.get_last_message()
                    else:
                        self.get_same_client(client_object).set_last_message(received)
                        output_message = client_object.get_public_IP() + " > " + self.get_same_client(client_object)\
                            .get_last_message()

                    print(output_message)

            time.sleep(1)