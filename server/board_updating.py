from threading import Thread
from tkinter import *
import time


class Updater(Thread):

    def __init__(self, clients_list, board_canvas):

        Thread.__init__(self)
        self.clients_list = clients_list
        self.board_canvas = board_canvas

    def run(self):

        while True:

            for i in range(len(self.clients_list)):

                client = self.clients_list[i]

                public_IP_label = Label(self.board_canvas, text=client.get_public_IP(), bd=3, relief=GROOVE, width=20, bg='#438BF6')
                local_IP_label = Label(self.board_canvas, text=client.get_local_IP(), bd=3, relief=GROOVE, width=20, bg='#438BF6')
                username_label = Label(self.board_canvas, text=client.get_username(), bd=3, relief=GROOVE, width=20, bg='#438BF6')
                network_username_label = Label(self.board_canvas, text=client.get_network_username(), bd=3, relief=GROOVE, width=21, bg='#438BF6')

                public_IP_label.grid(row=i+1, column=0)
                local_IP_label.grid(row=i+1, column=1)
                username_label.grid(row=i+1, column=2)
                network_username_label.grid(row=i+1, column=3)

            for i in range(len(self.clients_list), 100):

                public_IP_label = Label(self.board_canvas, text="", bd=3, relief=GROOVE, width=20, bg='#438BF6')
                local_IP_label = Label(self.board_canvas, text="", bd=3, relief=GROOVE, width=20, bg='#438BF6')
                username_label = Label(self.board_canvas, text="", bd=3, relief=GROOVE, width=20, bg='#438BF6')
                network_username_label = Label(self.board_canvas, text="", bd=3, relief=GROOVE, width=21, bg='#438BF6')

                public_IP_label.grid(row=i + 1, column=0)
                local_IP_label.grid(row=i + 1, column=1)
                username_label.grid(row=i + 1, column=2)
                network_username_label.grid(row=i + 1, column=3)

            time.sleep(5)