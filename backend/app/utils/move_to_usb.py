import shutil
import os



def move_to_usb():
    get_media =  os.listdir('/media/tempi')
    usb_path  = '/media/tempi/'+get_media[0]+'/'+'tempi_experiment.xlsx'
    shutil.move('tempi_experiment.xlsx',usb_path)

