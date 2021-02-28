# -*- coding:utf-8 -*-
from json import loads
from time import time
from zipfile import ZipFile
import os
import urllib.request as dlurl

# Save the name of the directory and the path to it into variables
directory = 'minecraft_datapacks_generator'
repo_owner = 'Vianpyro'
folder = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python39\\Lib' if os.name == 'nt' else '/usr/lib/python3.9'
exist = os.path.exists(f'{folder}\\{directory}') and os.path.isdir(f'{folder}\\{directory}')

def ask_user(querry) -> bool:
    return input(f'{querry}? [yes/no]: ')[0].lower() == 'y'

def download_repo(repo_owner:str, directory:str, version:str) -> bool:
    try:
        print(f'Downloading {directory} {version}...')
        dlurl.urlretrieve(f'https://github.com/{repo_owner}/{directory}/archive/{version}.zip', f'{directory}.zip')
    except:
        raise InterruptedError(f'Unable to download {directory} {version}...')
    else:
        print(f'Successfully downloaded {directory} {version}.')
        return True

def unzip(directory, destination) -> bool:
    with ZipFile(f'{directory}.zip', 'r') as zipf:
        try: zipf.extractall(destination)
        except: zipf.extractall()
        zipf.close()
        os.remove(f'{directory}.zip')
        return os.path.exists(f'{folder}\\{directory}') and os.path.isdir(f'{folder}\\{directory}')

def install(directory, folder, version) -> None:
    if download_repo(repo_owner='Vianpyro', directory='minecraft_datapacks_generator', version=version):
        if unzip(directory=directory, destination=folder):
            print(
                f'Successfully extracted {directory} {version} in "{folder}".',
                f'\nYou now have to delete the old version of the library and rename the most recent one "{directory}".'
            )
        else:
            os.rename(f'{folder}\\{directory}-{version}', f'{folder}\\{directory}')
            print(f'Successfully extracted and installed {directory} {version} in "{folder}".')

# Retrieve latest released version
try:
    resp = dlurl.urlopen(f'https://api.github.com/repos/{repo_owner}/{directory}/releases')
    data = loads(resp.read())[0]
    version = data['tag_name']
except:
    raise InterruptedError('Unable to retrieve latest released version.')

# Checking if the user already uses the latest version
try:
    from minecraft_datapacks_generator import __version__
except:
    install()
else:
    if version == __version__:
        print('You are already using the latest version.')
    elif ''.join([e for e in version.split('.') if e not in ['alpha', 'beta']]) < ''.join([e for e in __version__.split('.') if e not in ['alpha', 'beta']]):
        print('Version under development, you cannot download a later version.')
    else:
        # The user is not using the latest version : scan the user computer
        if exist:
            print(f'Found at: {folder}\\{directory}, replace this version with the latest release.')
        else:
            print('Unable to find the library.')
            if ask_user('Do you want to scan your computer to look for the folder'):
                found = False
                directory_list = str(folder + '\\site-packages').split('\\')
                tree = ['\\'.join(directory_list[:i + 1]) for i in range(len(directory_list))][::-1]

                try:
                    time0 = time()
                    HDDs = tree + [e + ':\\' for e in 'CDEFGHIJK' if os.path.exists(e + ':\\')]

                    for HDD in HDDs:
                        if not found:
                            for path, dirs, files in os.walk(HDD):
                                if folder + os.path.sep + directory in path:
                                    found = True
                                    print(f'Found at: {path} in {time() - time0:0.1} seconds.')
                                    break
                except OSError as e:
                    raise OSError('Unable to scan the computer.')
                else:
                    if not found:
                        print(f'Unable to locate "{directory}".')
                    print(f'Paste the "{directory}" folder in here: {folder}\\{directory}\\site-packages.')
        try:
            if ask_user(f'Would you like to install the latest version ({version})'):
                install()
        except:
            raise InterruptedError('Unable to resolve host name.')

input('Press "enter" to close this window.')
