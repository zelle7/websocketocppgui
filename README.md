# Simple GUI for debugging OCPP websocket messages - Work In prgoress
The project needs python3 to run and should have installed tkinter

## Run application
```bash
python run.py
```

### Development
There is a Pipfile in the root of the project which contains all the necessary dependencies. I've used wss://echo.websocket.org for testing, this will just return you the request sent

#### TODOs:
* Fix scrolling for log box (text box where the sent and received messages will be shown)
* automatically scroll to bottom on a new message added to the log box
* fix layout 
* add argparse to define a url etc on startup
* add the possiblity to give a client cert and server cert for the wss connection
* add more predefined messages
* Add a export button to store all the messages received
* Use the header of the dropbox
* Fix logging
* Add menu with export buttons, settings etc ...

#### UI 
The ui is build with the ui builder `pygubu-designer`. To start the designer simply call `pygubu-designer`
in your bash.

### Packaging 
To package the application into a single executable without python to be installed
you can call `pyinstaller --onefile --noconsole --add-data="uidef.ui:xml" --hidden-import tkinter --hidden-import pygubu run.py`
Make sure that `from pygubu.builder import ttkstdwidgets` is somewhere imported, otherwise you
would get an error.