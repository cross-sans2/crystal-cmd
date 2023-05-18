build_file:
	clear
	pyinstaller --onefile --name "Crystal cmd" main.py
	gnome-terminal -- 'dist/Crystal cmd'
