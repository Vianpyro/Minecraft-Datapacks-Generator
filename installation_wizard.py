# -*- coding:utf-8 -*-
import os
import subprocess
from time import time

directory = '\\minecraft_datapacks_generator'

if os.name == "nt":
    folder = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python39\\Lib'
    
    if os.path.exists(f'{folder}{directory}') and os.path.isdir(f'{folder}{directory}'):
        print('Found at:', f'{folder}{directory}, replace this version with the latest release.')
    else:
        if input('Do you want to scan your computer to look for the folder? [yes/no]: ')[0].lower() == 'y':
            found = False
            directory_list = str(folder + '\\site-packages').split('\\')
            tree = ['\\'.join(directory_list[:i + 1]) for i in range(len(directory_list))][::-1]
            HDDs = tree + [e + ':\\' for e in 'CDEFGHIJK' if os.path.exists(e + ':\\')]

            for HDD in HDDs:
                if not found:
                    time0 = time()
                    for path, dirs, files in os.walk(HDD):
                        if folder + directory in path:
                            found = True
                            print(f'Found at: {path} in {time() - time0:0.1} seconds.')
                            break
        print(f'Paste the "minecraft_datapack_generator" folder in here: {folder}{directory}.')
else:
    print('This operating system is not compatible with the installation wizard.')

input('Press "enter" to close this window.')
