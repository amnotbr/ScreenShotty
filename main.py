import platform
import win32gui
import win32ui
import win32con
import numpy

if platform.system() == "Windows":
    print("              RUNNING")
    print("------------------------------------")
else:
    print("WRONG PLATFORM")
    print("-------------------------------------")
    print("WINDOWS IS BETTER")
    
    
# getting the screenshot
def get_screenshot(x, y, width, height):
    hwnd = win32gui.GetDesktopWindow()
    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    
    # width and height of the screen, change asn needed 
    # WORKS LIKE PYAUTOGUI WIDTH AND HEIGHT WHEN SCREENSHOTTING
    x, y, width, height = x, y, width, height
    
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(screenshot)
    
    save_dc.BitBlt((0, 0), (width, height), mfc_dc, (x, y), win32con.SRCCOPY)
    
    # Convert the bitmap to a numpy array
    bmp_info = screenshot.GetInfo()
    bmp_str = screenshot.GetBitmapBits(True)
    img = numpy.frombuffer(bmp_str, dtype=numpy.uint8)
    img = img.reshape((bmp_info['bmHeight'], bmp_info['bmWidth'], 4))
    
    # Clean up resources
    win32gui.DeleteObject(screenshot.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)
    
    return img # returning the image
    