from pywinauto.application import Application
from pywinauto.findwindows import find_elements
from pywinauto.findwindows import find_windows
import time

# https://pywinauto.readthedocs.io/en/latest/HowTo.html
# https://github.com/pywinauto/pywinauto

# Listar elementos abertos
for element in find_elements():
    print(element)
    #print(dir(element))
    print('name',element.name)
    print('process_id',element.process_id)
    print('wm_get_ctrl_name',element.wm_get_ctrl_name)
    print('dump_window',element.dump_window)
    print('control_id',element.control_id)
    print('automation_id',element.automation_id)

for window in find_windows():
    print('window', window)
    print('dir->',dir(window))

# Listar processos

# capturar estado da janela browser

# app = Application().start("notepad.exe")
# app.UntitledNotepad.menu_select("Help->About Notepad")
# app.AboutNotepad.OK.click()
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
#opera2 = None
try:
    print('Abrindo...')
    notepad = Application().connect(title_re=".*Bloco de Notas", class_name="Notepad")
    notepad.UntitledNotepad.Edit.type_keys("o pitoco nao presta!", with_spaces = True)
    print('notepad ok')
    app = Application().connect(path=r"C:\Users\lucas\AppData\Local\Programs\Opera\opera.exe")
    print('app opera path ok')
    opera2 = Application().connect(title_re=".*Opera.*", class_name="Opera")
    print('opera 2 ok')
    dialogs = app.windows()
    # for win in dialogs:
    #     print(dialogs)
except :
    print(f'Algo deu errado - ')

time.sleep(2)
opera =  Application().connect(process = 9008)
#print(opera)
#print(dir(opera))
print('OK')
print(((app.window().print_control_identifiers())))
print(((app.window().actions)))

for window in app.windows():
    print(window)
    print(window.window_text)
    print(window.texts)
    print(window.menu_items)