import pyautogui
import webbrowser
import time
url = "https://www.roblox.com/home"
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(url)
time.sleep(5)
a = 0
while a < 3:
    a+1
    pyautogui.moveTo(1119,969,5)
    pyautogui.click()
    pyautogui.moveTo(1097,728,5)
    pyautogui.click()
    pyautogui.moveTo(843,968,5)
    pyautogui.click()
    pyautogui.typewrite("slm",interval=0.50)
    pyautogui.press("enter")
    pyautogui.typewrite("npyrsn",interval=0.50)
    pyautogui.press("enter")
    pyautogui.typewrite("nsllsn",interval=0.50)
    pyautogui.press("enter")
    #pyautogui.press("F5")
