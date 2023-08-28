import webbrowser

iurl = input("İndirmek istediğiniz bağlantının https://www sız halini atınız \nÖrnek = 'youtube.com/watch?v=bU9a3eggcE0' \n")
url = f"ss{iurl}"
print(url)
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)