import argparse
import datetime
import importlib
import json
from json import JSONDecodeError
from threading import Thread
from tkinter import messagebox
from pygubu.builder import ttkstdwidgets
from typing import Optional

from urls import validate_url, URLParseException

try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2

import logging

import pygubu
import websocket

logger = logging.getLogger('root')
logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

PREDEFINED_MESSAGE_MAP = {
    'Heartbeat': '[2, "uuid", "Heartbeat", {}]',
    'BootNotification': '[2, "uuid", "BootNotification", {"value":12}]',
}


class Application(pygubu.TkApplication):
    ws_thread: Thread
    wssurl: Optional[tk.Entry]
    send_button: Optional[tk.Button]
    connect_button: Optional[tk.Button]
    connection_status: Optional[tk.Label]
    data_to_send: Optional[tk.Text]
    log_box: Optional[tk.Text]
    predefined_messages: Optional[tk.Listbox]
    button_predefined_message: Optional[tk.Button]
    ws: Optional[websocket.WebSocketApp]

    def __init__(self, master=None):
        super().__init__(master)
        self.wssurl = None
        self.ws = None

    def _create_ui(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('uidef.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('base_frame', self.master)
        # fetch other elements we might need
        self.wss_url = builder.get_object('wssurl')
        self.send_button = builder.get_object('send_button')
        self.connect_button = builder.get_object('connect_button')
        self.connection_status = builder.get_object('connection_status')
        self.predefined_messages = builder.get_object('predefined_messages')
        self.button_predefined_message = builder.get_object('button_predefined_message')
        self.data_to_send = builder.get_object('data_to_send', self.master)

        self.log_box = builder.get_object('log_box', self.master)
        self.log_box_scrollbar = builder.get_object('log_box_scrollbar', self.master)
        self.log_box['yscrollcommand'] = self.log_box_scrollbar.set
        self.log_box_scrollbar['command'] = self.log_box.yview

        self.set_resizable()

        self.builder.connect_callbacks(self)
        logger.debug("_create_ui finished")

    def _init_after(self):
        """
        Loads the predefined messages and puts it as a selection into the predefined messages box
        :return:
        """
        for key in PREDEFINED_MESSAGE_MAP.keys():
            self.predefined_messages.insert(tk.END, key)

    def on_connect_clicked(self):
        """
        Triggered when a user clicks the connect button. If there is no connection running we connect to
        the websocket server and update the texts in ui to disconnect etc. If there is a connection
        we will disconnect from the websocket server.

        :return:
        """
        if self.ws:
            self.reset_state_after_socket_close()
            return

        url = self.wss_url.get()
        try:
            validate_url(url)
        except URLParseException as e:
            messagebox.showinfo('Message', 'Please provide a valid url: {}'.format(e))
            return

        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message_received,
                                         on_error=self.on_error_socket,
                                         on_close=self.on_close_socket)
        self.run_ws()
        logger.debug("on_connect_clicked")
        self.master.focus()
        self.connect_button.config(text="disconnect")
        self.connection_status.config(text="connected")
        self.send_button.config(state=tk.ACTIVE)

    def run_ws(self):
        """
        Run a the websocket client in a separate thread, as we would block the main UI thread otherwise
        :return: void
        """
        import threading
        self.ws_thread = threading.Thread(target=self.ws.run_forever)
        self.ws_thread.start()

    def on_send_button_clicked(self):
        """
        Click handler for send button. Will gather the content of the data_to_send element and send it to

        :return:
        """
        if not self.ws:
            messagebox.showinfo('Message', 'Please connect to a websocket server first')
            return
        message = self.data_to_send.get(1.0, tk.END)
        try:
            json.loads(message)
        except JSONDecodeError:
            messagebox.showerror("Invalid json", "Please provide a valid json object for sending")
            return
        self.write_to_text_box('> {}'.format(message))
        self.ws.send(data=message)

    def on_use_predefined_message_clicked(self):
        """
        Triggered when a user clicks the button beneath predefined messages. Looks up the message
        for the selection and paste it into the messages box, so that the user can still edit it.

        :return:
        """
        selection = self.predefined_messages.curselection()
        if not selection:
            messagebox.showerror('Nothing selected', "Please select a predefined message first")
        try:
            new_message = PREDEFINED_MESSAGE_MAP[self.predefined_messages.get(selection)]
        except KeyError:
            messagebox.showerror('Error on pasting', 'Could not find data for selection')
            return
        self.data_to_send.delete("1.0", tk.END)
        self.data_to_send.insert(tk.END, new_message)

    def write_to_text_box(self, message):
        """
        Writes a string to the log box text area
        :param message:
        :return:
        """
        now = datetime.datetime.now()
        message_to_print = '{} | {}'.format(now.isoformat(), message)
        if not message.endswith('\n'):
            message_to_print = '{}\n'.format(message)
        self.log_box.insert(tk.END, message_to_print)

    def on_close_socket(self):
        """
        Called if the websocket closes the connection
        :return:
        """
        self.write_to_text_box('connection closed')

    def on_error_socket(self, e):
        """
        Triggered if an error happens during the socket communication
        :param e:
        :return:
        """
        self.write_to_text_box('connection closed because of error {}'.format(e))

    def on_message_received(self, message):
        """
        Writes an incoming socket message to the log box.
        :param message:
        :return:
        """
        self.write_to_text_box('< {}'.format(message))

    def reset_state_after_socket_close(self):
        """
        Resets the state of the websocket and according gui elements after a connection close
        :return:
        """
        self.ws.close()
        self.connect_button.config(text="connect")
        self.connection_status.config(text="not connected")
        self.send_button.config(state=tk.DISABLED)
        self.ws = None
        self.ws_thread.join(1)


websocket.enableTrace(True)


if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser(description="Websocket OCPP GUI")
    parser.add_argument("--uri", help="websocket server uri will be set to client if set")
    parser.add_argument("--cafile", nargs="?", help="SSL CA file")
    parser.add_argument("--certfile", nargs="?", help="SSL client certificate file")
    parser.add_argument("--keyfile", nargs="?", help="SSL private key file")
    parser.add_argument("--no-check-hostname", action="store_true", help="disable SSL certificate hostname check")
    parser.add_argument("--read-ui-file", action="store_true", help="Reads the ui from a ")
    args = parser.parse_args()

    root = tk.Tk()
    # uidef = importlib.util.find_spec('uidef')
    # if not args.read_ui_file and not uidef:
    #     print("No ui def files defined")
    #     exit(1)

    app = Application(root)

    logger.debug("Start application now")
    root.mainloop()
