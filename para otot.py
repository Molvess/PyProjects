import webbrowser
import pyautogui
url = "https://ay.link/btkake"

pyautogui.moveTo(623,221,5)
pyautogui.click()
pyautogui.moveTo(128,3,5)
pyautogui.click()
pyautogui.moveTo(623,221,5)
pyautogui.click()

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)



