class Client:

    def __init__(self, received, socket):
        splitted = received.split(",")
        self.public_IP = splitted[0]
        self.local_IP = splitted[1]
        self.username = splitted[2]
        self.network_username = splitted[3]
        self.last_message = splitted[4]
        self.socket = socket

    def is_same_client(self, client):
        if self.get_public_IP() == client.get_public_IP() and self.get_local_IP() == client.get_local_IP():
            return True
        else:
            return False

    def set_last_message(self, message):
        self.last_message = message.split(",")[4]

    def get_public_IP(self):
        return self.public_IP

    def get_local_IP(self):
        return self.local_IP

    def get_username(self):
        return self.username

    def get_network_username(self):
        return self.network_username

    def get_socket(self):
        return self.socket

    def get_last_message(self):
        return self.last_message

    def send_message(self, message):
        try:
            message = message.encode()
            self.socket.send(message)
        except:
            pass