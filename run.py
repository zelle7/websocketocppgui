try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2

import pygubu
import websocket


class Application(pygubu.TkApplication):
    def _create_ui(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('uidef.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('base_frame', self.master)

    def on_connect_clicked(self):
        self.ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                    on_message=self.write_to_text_box,
                                    on_error=self.write_to_text_box,
                                    on_close=self.write_to_text_box)

    def write_to_text_box(self, message):
        print(message)


websocket.enableTrace(True)
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
