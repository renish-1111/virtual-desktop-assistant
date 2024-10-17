import pygetwindow as gw
from pywinauto.application import Application

def close_current_app():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            app = Application().connect(handle=active_window._hWnd)
            app.kill()
            return f"Closed {active_window.title} successfully."
        else:
            return "No active window found."
    except Exception as e:
        return f"Could not close the active application. Error: {e}"
