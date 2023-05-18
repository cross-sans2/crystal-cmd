#!/usr/bin/env python
import cmd, os, shutil, subprocess
import mod2 as bt# original made by me on a diffirent profile: https://github.com/cross-sans/betterTEXT/blob/main/mod/mod2.py
from PIL import Image
import signal
from colorit import init_colorit, background
init_colorit()


def image(imgsrc):
    try:
        image = Image.open(imgsrc)
        terminal_size = shutil.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = os.get_terminal_size().lines

        # Calculate the aspect ratios of the terminal and the image
        terminal_aspect_ratio = terminal_width / terminal_height
        image_aspect_ratio = image.width / image.height

        # Resize the image while preserving the aspect ratio using Lanczos resampling
        if image_aspect_ratio > terminal_aspect_ratio:
            new_width = terminal_width
            new_height = int(new_width / image_aspect_ratio)
        else:
            new_height = terminal_height
            new_width = int(new_height * image_aspect_ratio)

        image = image.resize((new_width, new_height), resample=Image.LANCZOS)

        width, height = image.size
        for y in range(height):
            for x in range(width):
                print(background(' ', image.getpixel((x, y))), end='')
            print()

    except FileNotFoundError as e:
        print(f"error: {e}")




class Main(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        #os.chdir('/home')
        self.prompt = f"{bt.colored(os.getcwd(),'green')}:>"
        self.ver = "0.0.5"
        print(f"{bt.multicolor_text('Crystal cmd v'+self.ver,['yellow','red','blue'])}")


    def do_cd(self, arg):
        try:
            os.chdir(arg)
        except FileNotFoundError:
            print("Directory not found: {}".format(arg))
        except NotADirectoryError:
            print("Not a directory: {}".format(arg))
        except PermissionError:
            print("Permission denied: {}".format(arg))
        else:
            self.prompt = f"{bt.colored(os.getcwd(),'green')}:>"

    def do_clear(self,args):
        bt.clear()
    
    def do_image(self, imgsrc):
        image(imgsrc)
    
    def do_ls(self, arg):
        try:
            files = os.listdir(arg) if arg else os.listdir(".")
            for file in files:
                print(file)
        except FileNotFoundError:
            print("Directory not found: {}".format(arg))
        except NotADirectoryError:
            print("{} is not a directory".format(arg))
        except PermissionError:
            print("Permission denied: {}".format(arg))

    def do_quit(self, arg):
        return True

    def do_mkdir(self, names):
        dnames = names.split(' ')
        for name in dnames:
            try:
                os.mkdir(name)
            except FileExistsError:
                print("Directory already exists: {}".format(name))
            except PermissionError:
                print("Permission denied: {}".format(name))

    def do_touch(self, names):
        dnames = names.split(' ')
        for name in dnames:
            try:
                with open(name, 'w') as f:
                    f.write('')
            except PermissionError:
                print("Permission denied: {}".format(name))

    def do_run(self, app):
        try:
            subprocess.run(app, shell=True)
        except FileNotFoundError as e:
            print(f"error: {bt.colored(e,'red')}")

    def default(self, arg):
        print("Command not recognized:", arg)

    def cmdloop(self, intro=None):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            super().cmdloop(intro)
        except KeyboardInterrupt:
            print("^C")

if __name__ == '__main__':
    Main().cmdloop()
