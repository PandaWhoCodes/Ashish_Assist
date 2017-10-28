import ctypes
def showAlert():
    ctypes.windll.user32.MessageBoxW(0, "Time to skeedadle", "Go human GO!!", 1)
