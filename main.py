#!/usr/bin/env python
import cmd, os, shutil, subprocess
import mod2 as bt# original made by me on a diffirent profile: https://github.com/cross-sans/betterTEXT/blob/main/mod/mod2.py
from PIL import Image
import signal
from colorit import init_colorit, background
init_colorit()
import stat
import glob
from handler import handle_error
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
        error_message = f"Error: {e}"
        handle_error(error_message, self.error_file)


class Main(cmd.Cmd):
    def __init__(self):
        """
        Initialize the command-line interface.

        This function sets up the prompt, version number, and prints a welcome message.
        """
        # Define the error file path
        self.error_file = os.path.join(os.path.expanduser('~'), 'Crystal', 'error_log.txt')

        self.HOME_DIR = os.path.expanduser('~')
        error = False
        current = os.getcwd()
        try:
            os.chdir(f'{self.HOME_DIR}/Crystal')
        except:
            os.mkdir(f"{self.HOME_DIR}/Crystal")
        os.chdir(current)
        print(f"any and all Crystal CMD related errors will go to {self.HOME_DIR}/Crystal")
        cmd.Cmd.__init__(self)
        self.prompt = f"{bt.colored(os.getcwd(),'green')}:>"
        self.ver = "0.1.0"
        print(f"{bt.multicolor_text('Crystal cmd v'+self.ver,['yellow','red','blue'])}")
    def do_ver(self, arg):
        print(f"{bt.multicolor_text('Crystal cmd v'+self.ver,['yellow','red','blue'])}")

    def complete_image(self, text, line, begidx, endidx):
        """
        Tab completion for the 'image' command.

        This function only returns image files for tab completion.
        """
        image_files = glob.glob(text + '*.png') + glob.glob(text + '*.jpg') + glob.glob(text + '*.jpeg')
        image_files = [file for file in image_files if os.path.isfile(file)]
        return image_files
    def complete_cd(self, text, line, begidx, endidx):
        """
        Tab completion for the 'cd' command.
        """
        dir_names = glob.glob(text + '*/')  # Only match directories
        return dir_names

    def complete_ls(self, text, line, begidx, endidx):
        """
        Tab completion for the 'ls' command.
        """
        dir_files = glob.glob(text + '*/')  # Only match directories
        return dir_files
    def do_cd(self, arg):
        """
        Change the current working directory.

        Parameters:
        - arg (str): The path to the target directory.

        This function changes the current working directory to the specified directory.

        Raises:
        - FileNotFoundError: If the specified directory is not found.
        - NotADirectoryError: If the specified path is not a directory.
        - PermissionError: If permission is denied for accessing the specified directory.
        """
        if arg:
            try:
                os.chdir(arg)
            except FileNotFoundError as e:
                print("Directory not found: {}".format(arg))
                error_message = f"Directory not found: {e}"
                handle_error(error_message, self.error_file)

            except NotADirectoryError as e:
                print("Not a directory: {}".format(arg))
                error_message = f"Not a directory: {e}"
                handle_error(error_message, self.error_file)

            except PermissionError as e:
                print("Permission denied: {}".format(arg))
                error_message = f"Permission denied: {e}"
                handle_error(error_message, self.error_file)
            else:
                self.prompt = f"{bt.colored(os.getcwd(),'green')}:>"
        else:
            os.chdir(self.HOME_DIR)

    def do_clear(self, args):
        """
        Clear the terminal screen.

        This function clears the terminal screen.
        """
        bt.clear()

    def do_image(self, imgsrc):
        """
        Display an image in the terminal.

        Parameters:
        - imgsrc (str): The path to the image file.

        This function calls the `image` function to display the specified image in the terminal.

        Usage: image <imgsrc>
        """
        image(imgsrc)

    def do_ls(self, arg):
        """
        List files in a directory.

        Parameters:
        - arg (str): The path to the target directory. If not provided, the current directory is used.

        This function lists the files in the specified directory or the current directory if no directory is specified.

        Raises:
        - FileNotFoundError: If the specified directory is not found.
        - NotADirectoryError: If the specified path is not a directory.
        - PermissionError: If permission is denied for accessing the specified directory.
        """
        try:
            files = os.listdir(arg) if arg else os.listdir(".")
            for file in files:
                file_path = os.path.join(arg, file) if arg else file
                if not os.path.isfile(file_path):
                    print(bt.colored(file, 'blue'))
                else:
                    mode = os.stat(file_path).st_mode
                    if mode & stat.S_IXUSR or mode & stat.S_IXGRP or mode & stat.S_IXOTH:
                        print(bt.colored(file, 'green'))
                    else:
                        print(file)
        except FileNotFoundError as e:
            print("Directory not found: {}".format(arg))
            error_message = f"Directory not found: {e}"
            handle_error(error_message, self.error_file)

        except NotADirectoryError as e:
            print("{} is not a directory".format(arg))
            error_message = f"is not a directory: {e}"
            handle_error(error_message, self.error_file)

        except PermissionError as e:
            print("Permission denied: {}".format(arg))
            error_message = f"Permission denied: {e}"
            handle_error(error_message, self.error_file)

    def do_close(self, arg):
        """
        Quit the command-line interface.

        This function exits the command-line interface.

        Usage: quit
        """
        return True

    def do_mkdir(self, names):
        """
        Create directories.

        Parameters:
        - names (str): The names of the directories to create, separated by spaces.

        This function creates directories with the specified names.

        Raises:
        - FileExistsError: If a directory with the same name already exists.
        - PermissionError: If permission is denied for creating the directory.
        """
        dnames = names.split(' ')
        for name in dnames:
            try:
                os.mkdir(name)
            except FileExistsError as e:
                print("Directory already exists: {}".format(name))
                error_message = f"Directory already exists: {e}"
                handle_error(error_message, self.error_file)

            except PermissionError as e:
                print("Permission denied: {}".format(name))
                error_message = f"Permission denied: {e}"
                handle_error(error_message, self.error_file)

    def do_touch(self, names):
        """
        Create empty files.

        Parameters:
        - names (str): The names of the files to create, separated by spaces.

        This function creates empty files with the specified names.

        Raises:
        - PermissionError: If permission is denied for creating the file.
        """
        dnames = names.split(' ')
        for name in dnames:
            try:
                with open(name, 'w') as f:
                    f.write('')
            except PermissionError as e:
                print("Permission denied: {}".format(name))
                error_message = f"Permission denied: {e}"
                handle_error(error_message, self.error_file)



    def default(self, arg):
        """
        Handle unrecognized commands.
        """
        try:
            subprocess.run(arg, shell=True)
        except NameError as e:
            error_message = f"An error occurred: {e}"
            handle_error(error_message, self.error_file)
    def cmdloop(self, intro=None):
        """
        Run the command-loop.

        Parameters:
        - intro (str): Optional introduction text.

        This function starts the command-loop, ignoring the SIGINT (Ctrl+C) signal.
        It handles keyboard interrupts gracefully and prints "^C" when interrupted.
        """
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            super().cmdloop(intro)
        except:
            print("fatal error, console killed")
            error_message = "fatal error, console killed"
            handle_error(error_message,self.error_file)
            input()


if __name__ == '__main__':
    Main().cmdloop()
