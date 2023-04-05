import select
import webbrowser
import pyperclip
import pyautogui
import time
from colorama import Fore, Style

documents = open("ip_google.txt","r")
documents = documents.read().split('\n')

election = input (Fore.GREEN + "Inserte nombre de la herramienta que se quiera usar para el analisis ip: " + Fore.YELLOW +
                 """\n
                 1 - Synmantec 
                 2 - AbuseIP
                 3 - Virustotal: \n""" + Style.RESET_ALL + "Seleccione la herramienta ➜")
if election=="1":
    for ip in documents:
        webbrowser.open_new("https://sitereview.bluecoat.com/#/")
        time.sleep(2)
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15 )
        pyautogui.press("enter")

elif election=="2":
    for ip in documents:
        webbrowser.open_new("https://www.abuseipdb.com/")
        time.sleep(4)
        for i in range(15):
            pyautogui.press('tab')
            pyperclip.copy(ip)
            pyautogui.hotkey('ctrl', 'v', interval = 0.15)
            pyautogui.press("enter")
    
elif election=="3":
    for ip in documents:
        webbrowser.open_new("https://www.virustotal.com/gui/home/search")
        time.sleep(2)
        for i in range(6):
            pyautogui.press('tab')
            pyperclip.copy(ip)
            pyautogui.hotkey('ctrl', 'v', interval = 0.15)
            pyautogui.press("enter")
else:
    print("ERROR! Solo adminte los siguientes valores 1,2,3" )
