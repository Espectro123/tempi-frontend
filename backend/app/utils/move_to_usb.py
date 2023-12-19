import shutil
import os
import psutil

def find_usb_drive():
    usb_drive = None
    all_drives = psutil.disk_partitions()
    for drive in all_drives:
        if 'removable' in drive.opts:
            usb_drive = drive.mountpoint
            break
    return usb_drive

def move_to_usb():
    usb_path = find_usb_drive()
    print(usb_path)
    file_path = 'tempi_experiment.xlsx'
    if usb_path:
        try:
            shutil.move(file_path, os.path.join(usb_path, os.path.basename(file_path)))
            print("File moved successfully to USB drive:", usb_path)
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied. Make sure you have the necessary permissions.")
    else:
        print("USB drive not found.")