from termcolor import colored
import webbrowser, os, sys
__version__ = "betterTEXT v1.2 Crystal edition"

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
#clear is not on the original module

def color_text(text, color):
    """
    Returns colored text using the specified color.
    """
    return colored(text, color)

def println(text, color=None):
    """
    Prints formatted text to the console with optional color.
    """
    if color:
        text = colored(text, color)
    print(text)

def request(prompt, color=None):
    """
    Prompts the user for input with optional color and returns the input value.
    """
    if color:
        prompt = colored(prompt, color)
    return input(prompt)


def multicolor_text(text, colors=None):
    """
    Returns the specified text with different colors.
    """
    if colors:
        colored_chars = [colored(char, colors[i % len(colors)]) for i, char in enumerate(text)]
        return "".join(colored_chars)
    else:
        return text
def multicolor_input(prompt, colors=None):
    """
    Prompts the user for input with the specified prompt and colors.
    """
    if colors:
        prompt = multicolor_text(prompt, colors)
    return input(prompt)



def search_online(query):
    """
    Searches for the specified query online using the default web browser.
    """
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
