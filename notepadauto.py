from pywinauto.application import Application
from pywinauto.findwindows import find_elements
import time

# https://pywinauto.readthedocs.io/en/latest/HowTo.html
# https://github.com/pywinauto/pywinauto

# Listar elementos abertos
print(find_elements())

# Listar processos

# capturar estado da janela browser

# app = Application().start("notepad.exe")
# app.UntitledNotepad.menu_select("Help->About Notepad")
# app.AboutNotepad.OK.click()
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
try:
    notepad = Application().connect(title_re=".*Bloco de Notas", class_name="Notepad")
    notepad.UntitledNotepad.Edit.type_keys("o pitoco nao presta!", with_spaces = True)
except :
    print(f'Algo deu errado - ')
opera2 = Application().connect(title_re=".*Opera Internet Browser", class_name="Opera")
app = Application().connect(path=r"C:/Users/lucas/AppData/Local/Programs/Opera/opera.exe")
print('Abrindo...')
dialogs = app.windows()
for win in dialogs:
    print(dialogs)
time.sleep(4)
opera =  app.window(title_re = ".*Opera.*")
print('OK')
print((opera.MenuItems()))
# print(dir(opera.Properties.OK))