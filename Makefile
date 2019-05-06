clean:
	rm -rf dist/
	rm -rf build/
	rm -f run.spec

copygui:
	 echo uidef=\"\"\" > uidef.py && cat uidef.ui >> uidef.py && echo \"\"\" >> uidef.py

build:
	pyinstaller --onefile --noconsole --add-data="uidef.ui:xml" --hidden-import tkinter --hidden-import pygubu run.py

