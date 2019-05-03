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
* Add description to buld an standalone executable
#### UI 
The ui is build with the ui builder `pygubu-designer`. To start the designer simply call `pygubu-designer`
in your bash.