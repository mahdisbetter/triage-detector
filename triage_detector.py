import ctypes
import os

def detect():
    buffer_size = 260
    buffer = ctypes.create_unicode_buffer(buffer_size)
    ctypes.windll.user32.SystemParametersInfoW(0x0073, buffer_size, buffer, 0)
    wallpaper_path = buffer.value
    
    if os.path.isfile(wallpaper_path):
        file_size = os.path.getsize(wallpaper_path)
        if file_size == 24811:
            return True
    else:
        return False

is_triage = detect()
if is_triage:
    print('triage detected')
    exit()
