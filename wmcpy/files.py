import os


def make_directory(name, path:str='') -> None:
    '''
    This functions creates a directory

    :param name:    The name of the directory to create.
    :param path:    The path where the directory has to be created.
    :return:        None or OS-Error if the directory could not be created.
    '''
    try:
        os.mkdir(f'{path}{name}')
    except OSError:
        raise OSError(f'Failed to create the directory "{name}".')
    else:
        print(f'Successfuly created the directory "{name}".')

def create_file(name, path:str='', content:(str, list, dict)='') -> None:
    '''
    This functions creates a file

    :param name:    The name of the file to create.
    :param path:    The path where the file has to be created.
    :param content: The content to write in the created file.
    :return:        None or OS-Error if the file could not be created.
    '''
    with open(f'{path}{name}', 'w') as f:
        if isinstance(content, str):
            f.write(content)
        elif isinstance(content, list):
            for line in content:
                f.write(f'{line}\n')
        elif isinstance(content, dict):
            for line in str(content).replace("'", '"').lower():
                f.write(f'{line}')
        else:
            raise TypeError(f'Argument "content" must be of type "str" or "list" not {type(content)}!')
        print(f'Successfuly created the file "{name}".')
        f.close()

def create_pack_meta(minecraft_version:str='1.6.1', description:str=None, author:str=None) -> str:
    '''
    This function helps with creating the string of a "pack.mcmeta" file ready to be written.
    
    :param minecraft_version:   The version of Minecraft in which the user's server runs.
    :param description:         A short description of the uses of the Datapack the user wants to make.
    :param author:              The user's name to write into the "pack.mcmeta".
    :return:                    String of a "pack.mcmeta" file.
    '''
    default_pack_format = 7
    minecraft_version_to_pack_format = {
        '1.6.1': 1, '1.6.2': 1, '1.6.4': 1,
        '1.7.2': 1, '1.7.4': 1, '1.7.5': 1, '1.7.6': 1, '1.7.7': 1, '1.7.8': 1, '1.7.9': 1, '1.7.10': 1,
        '1.8': 1, '1.8.1': 1, '1.8.2': 1, '1.8.3': 1, '1.8.4': 1, '1.8.5': 1, '1.8.6': 1, '1.8.7': 1, '1.8.8': 1, '1.8.9': 1,
        '1.9': 2, '1.9.1': 2, '1.9.2': 2, '1.9.3': 2, '1.9.4': 2,
        '1.10': 2, '1.10.1': 2, '1.10.2': 2,
        '1.11': 3, '1.11.1': 3, '1.11.2': 3,
        '1.12': 3, '1.12.1': 3, '1.12.2': 3,
        '1.13': 4, '1.13.1': 4, '1.13.2': 4,
        '1.14': 4, '1.14.1': 4, '1.14.2': 4, '1.14.3': 4, '1.14.4': 4,
        '1.15': 5, '1.15.1': 5, '1.15.2': 5,
        '1.16': 5, '1.16.1': 5,
        '1.16.2': 6, '1.16.3': 6, '1.16.4': 6, '1.16.5': 6,
        '1.17': 7, '1.17+': 7
    }

    if minecraft_version in minecraft_version_to_pack_format:
        pack_format = minecraft_version_to_pack_format[minecraft_version]
    else:
        raise Warning(f'This version of Minecraft seems to have no pack format defined:\nSet to {default_pack_format} by default.')

    description = description
    author = author

    return str(
        {
            "pack": {
                "author": author,
                "description": description,
                "pack_format": pack_format
            }
        }
    ).replace("'", '"')


def import_from_file(path, extension='mcfunction') -> (str, None):
    '''
    This functions help with importing files instead of writing them.
    The files has to exist on the user's computer to be imported.

    :param path:        The path where the resource has to be find.
    :param extension:   The extension of the resource [e.g. ".mcfunction", ".json", ".dat"].
    :return:            None or OS-Error if the resource can not be found or read, a string containing the content of the imported file otherwise.
    '''
    try:
        with open(f'{path}.{extension}', 'r') as f:
            r = [line.replace('\n', '') for line in f if line not in ['', ' ', '\n']]
            f.close()
        return r
    except:
        raise ValueError(f'Could not read the file {path}.{extension}')
