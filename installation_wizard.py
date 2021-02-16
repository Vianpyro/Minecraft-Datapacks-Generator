# -*- coding:utf-8 -*-
import os
import subprocess
from time import time

directory = '\\minecraft_datapacks_generator'

if os.name == "nt":
    folder = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python39\\Lib'
    
    if os.path.exists(f'{folder}{directory}') and os.path.isdir(folder):
        print('Found at:', f'{folder}{directory}, replace this version with the latest release.')
    else:
        if input('Do you want to scan your computer to look for the folder? [yes/no]: ')[0].lower() == 'y':
            found = False
            HDDs = ['\\'.join(str(folder + '\\site-packages').split('\\')[:len(folder.split('\\'))-i+2])
                for i in range(4) if i != 0] + [e + ':\\' for e in 'CDEFGHIJK' if os.path.exists(e + ':\\')]

            for HDD in HDDs[:3]:
                if not found:
                    print('Walking in', HDD)
                    time0 = time()
                    for path, dirs, files in os.walk(HDD):
                        if folder + directory in path:
                            found = True
                            print('Found at:', path, 'in', time() - time0, 'seconds.')
                            break
        print(f'Paste the "minecraft_datapack_generator" folder in here: {folder}{directory}.')
else:
    print('This operating system is not compatible with the installation wizard.')

input('Press "enter" to close this window.')