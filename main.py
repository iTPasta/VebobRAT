from receiver import Receiver

clients_list = []

receiver_thread = Receiver(clients_list)

receiver_thread.start()