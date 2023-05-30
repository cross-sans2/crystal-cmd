from termcolor import colored
import webbrowser
import sys
import time

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

def delay(text, delay_time, color=None, print_all=False):
    """
    Prints each part of the text with a delay.
    """
    if color:
        text = color_text(text, color)
    parts = text.split("|")
    for part in parts:
        if print_all:
            for letter in part:
                print(letter, end="", flush=True)
                time.sleep(delay_time)
        else:
            println(part, color)
            time.sleep(delay_time)


def outprint(text, sec, color=None):
  """
    Prints formatted text to the console with optional color.
    """
  if color:
    text = colored(text, color)
  time.sleep(sec)
  print(text)


def request(prompt, color=None):
  """
    Prompts the user for input with optional color and returns the input value.
    """
  if color:
    prompt = colored(prompt, color)
  return input(prompt)


def intrequest(prompt, color=None):
  """
  prompts the user for a interger value, with optional text
  """
  if color:
    prompt = colored(prompt, color)
  try:
    return int(input(prompt))
  except:
    pass



def multicolor_text(text, colors=None):
    """
    Returns the specified text with different colors.
    """
    if colors:
        colored_chars = [colored(char, colors[i % len(colors)]) for i, char in enumerate(text)]
        return "".join(colored_chars)
    else:
        return text

def big_text(text):
  return colored(text, attrs=["bold"])


def small_text(text):
    return colored(text, attrs=["dim"])

def multicolor_input(prompt, colors=None):
  if colors:
    prompt = multicolor_text(prompt, colors)
  return input(prompt)


def search_online(query):
  """
    Searches for the specified query online using the default web browser.
    """
  url = f"https://www.google.com/search?q={query}"
  webbrowser.open(url)


println('thanks for using betterTEXT, and thanks for trusting data-finder',
        "green")
def overwrite(func):
  """
    A decorator function that can be used to overwrite existing functions.
  """
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  wrapper.__name__ = func.__name__
  return wrapper
