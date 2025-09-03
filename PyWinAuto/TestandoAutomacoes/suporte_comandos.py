import win32com.client

window = win32com.client.Dispatch("Word.Application")

window.Visible=0

# window.WindowState = win32com.client.constants.wdWindowStateMinimize
window.WindowState = win32com.client.constants.wdWindowStateMaximize