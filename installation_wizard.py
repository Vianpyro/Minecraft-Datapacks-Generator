# -*- coding:utf-8 -*-
import os
from time import time

# Save the name of the directory and the path to it into variables
directory = '\\minecraft_datapacks_generator2'
folder = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python39\\Lib' if os.name == 'nt' else '/usr/lib/python3.9'

if os.path.exists(f'{folder}{directory}') and os.path.isdir(f'{folder}{directory}'):
    print(f'Found at: {folder}{directory}, replace this version with the latest release.')
else:
    if input('Do you want to scan your computer to look for the folder? [yes/no]: ')[0].lower() == 'y':
        found = False
        directory_list = str(folder + '\\site-packages').split('\\')
        tree = ['\\'.join(directory_list[:i + 1]) for i in range(len(directory_list))][::-1]

        try:
            time0 = time()
            HDDs = tree + [e + ':\\' for e in 'CDEFGHIJK' if os.path.exists(e + ':\\')]

            for HDD in HDDs:
                if not found:
                    print('walking in', HDD)
                    for path, dirs, files in os.walk(HDD):
                        if folder + directory in path:
                            found = True
                            print(f'Found at: {path} in {time() - time0:0.1} seconds.')
                            break
        except OSError:
            raise OSError('Unable to scan your computer.')
        else:
            print(f'Paste the "minecraft_datapack_generator" folder in here: {folder}{directory}.')

input('Press "enter" to close this window.')
