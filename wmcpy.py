import os
from shutil import rmtree
from time import time


class Selector:
    def __init__(self, target_entity='@s',
                 advancements=None,
                 distance=None, dx=None, dy=None, dz=None,
                 entity_type=None,
                 gamemode=None, level=None, limit=None,
                 name=None, nbt=None,
                 scores=None, sort=None,
                 tag=None, team=None,
                 x=None, x_rotation=None,
                 y=None, y_rotation=None,
                 z=None
    ):
        self.target_entity = target_entity if target_entity in ('@a', '@e', '@p', '@r', '@s') else '@s'
        args = [
            ('advancements', advancements),
            ('distance', distance), ('dx', dx), ('dy', dy), ('dz', dz),
            ('entity_type', entity_type),
            ('gamemode', gamemode),
            ('level', level), ('limit', limit), ('limit', limit),
            ('name', name), ('nbt', nbt),
            ('scores', scores), ('sort', sort),
            ('tag', tag), ('team', team),
            ('x', x), ('x_rotation', x_rotation),
            ('y', y), ('y_rotation', y_rotation),
            ('z', z)
        ]
        self.args = [element for element in args if element[1] is not None]

    def __str__(self):
        r = self.target_entity + '['
        if len(self.args) == 0:
            r += ']'
        elif len(self.args) == 1:
            r += f'{self.args[-1][0]}={self.args[-1][1]}]'
        else:
            for i in range(len(self.args) - 2):
                r += f'{self.args[i][0]}={self.args[i][1]},'
            r += f'{self.args[-1][0]}={self.args[-1][1]}]'
        return r


class Datapack:
    def __init__(self, title, path=None, author="Vianpyro's datapack generator", pack_meta=None, content=None, auto_compile=False, auto_replace=False):
        """
        Initialisation of the Datapack.
        A datapack is a Minecraft folder in which a server administrator puts commands and rules
            to change the behavior of the game as much as desired.

        :param path:        The title where the datapack should be generated.
        :param title:       The title of the datapack.
        :param author:      The author of the datapack.
        :param pack_meta:   The content of the "pack.mcmeta".
        :param content:     The code the user writes in their datapack.
        :return:            None
        """
        # Set the title to lower case
        self.title = title.lower()

        # Checking if the path given is valid.
        if path is None:
            self.path = ''
        elif path[-1] == os.path.sep:
            self.path = path
        else:
            self.path = path + os.path.sep

        # Is this datapack new?
        self.exists = os.path.exists(self.path + self.title)
        self.replace = auto_replace

        if self.exists and not auto_replace:
            self.replace = input(f'{title} already exists, do you want to replace it? [yes/no]: ')[0].lower() == 'y'


        # Check if datapack format is correct.
        if not isinstance(title, str):
            raise TypeError(f'Argument "title" must be of type "str" not {type(title)}!')

        if not isinstance(author, str):
            raise TypeError(f'Argument "author" must be of type "str" not {type(author)}!')

        if pack_meta is not None and not isinstance(pack_meta, dict):
            raise TypeError(f'Argument "meta" must be of type "dict" not {type(pack_meta)}!')

        elif content is not None and not isinstance(content, dict):
            raise TypeError(f'Argument "content" must be of type "dict" not {type(content)}!')

        '''
        Save the title to lower case because of Minecraft datapack structure requiering lower case characters.
        Save the subfolder without spaces in between words to recall the functions easier.
        '''
        self.subfolder_title = self.title.replace(' ', '_')
        self.author = author
        self.pack_meta = pack_meta
        self.content = content

        if auto_compile:
            self.compile()

    def compile(self):
        '''
        This function compiles the parameters entered by the user to create a Minecraft Datapack.
        Probably the most important function of this program/library.

        :return: None or Error
        '''
        # Removing or not the older datapack with the same name (if it exists)
        if self.exists:
            if not self.replace:
                raise ValueError('Could not replace previous datapack.')
            else:
                try:
                    rmtree(self.path + self.title)
                except:
                    print(f'Failed to delete the directory "{self.title}".')
                else:
                    print(f'Successfuly deleted the directory "{self.title}".')

        # Starting the translation into the datapack
        print('Generating the datapack, this might take a few seconds...')
        time_stamp = time()

        if not self.exists or self.replace:
            # Create the datapack directory
            make_directory(self.title, self.path)

            # Create the "pack.mcmeta" file
            if self.pack_meta == None:
                print('No "pack.mcmeta" was generated!')
            else:
                create_file(
                    'pack.mcmeta', f'{self.path}{self.title}/',
                    str(create_pack_meta(
                        self.pack_meta['minecraft_version'],
                        self.pack_meta['description'],
                        self.author
                    ))
                )

            if self.content == None:
                print('No content was generated!')
            else:
                # Create the data directory containing every modification brung by the datapack
                make_directory('data', f'{self.path}{self.title}/')
                make_directory(self.subfolder_title, f'{self.path}{self.title}/data/')

                for key in self.content:
                    directory_name = f'{self.path}{self.title}/data/{self.subfolder_title}/{key}/'
                    
                    if key in [
                        'advancements', 'dimension_type', 'dimension', 'item_modifiers‌'
                        'loot_tables', 'functions', 'predicates', 'recipes'
                    ] and self.content[key] is not None:
                        # Create the key folder
                        print(f'Generating {key} files...')
                        make_directory(directory_name)
                        
                        if key == 'functions':
                            for function_file in self.content[key]:
                                create_file(
                                    f'{function_file}.mcfunction', directory_name,
                                    self.content[key][function_file]
                                )
                        else:
                            print('Be careful, this kind of file is not verified by this program and may contain some errors:', key)
                            for json_file in self.content[key]:
                                create_file(
                                    f'{json_file}.json', directory_name,
                                    self.content[key][json_file]
                                )

                        print(f'Successfuly generated {key} files.')
                    elif self.content[key] is None:
                        print(f'No file was generated for "{key}".')
                    else:
                        print(f'Failed to create {key} files : {key} is not supported (yet?).')
                
                # Create the main(tick) and load files
                make_directory('minecraft', f'{self.path}{self.title}/data/')
                make_directory('tags', f'{self.path}{self.title}/data/minecraft/')
                make_directory('functions', f'{self.path}{self.title}/data/minecraft/tags/')
                
                if os.path.exists(f'{self.path}{self.title}/data/{self.subfolder_title}/functions/load.mcfunction'):
                    create_file(
                        'load.json', f'{self.path}{self.title}/data/minecraft/tags/functions/',
                        f'{{"values": ["{self.subfolder_title}:load"]}}'
                    )
                if os.path.exists(f'{self.path}{self.title}/data/{self.subfolder_title}/functions/main.mcfunction'):
                    create_file(
                        'tick.json', f'{self.path}{self.title}/data/minecraft/tags/functions/',
                        f'{{"values": ["{self.subfolder_title}:main"]}}'
                    )

        print(f'Successfuly generated the datapack in {time() - time_stamp:0.1} seconds :).')

def make_directory(name, path=''):
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

def create_file(name, path='', content=''):
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


def Raycast(datapack_name, function_name, distance=20, step=0.3, goal=None, output=None, display_particle=None):
    return [
        f'particle {display_particle} ~ ~ ~ 0 0 0 0 1 normal @a' if display_particle is not None else None,
        f'{goal} run {output}' if goal is not None else None,
        f'execute if entity @s[distance=..{distance}] positioned ^ ^ ^{step} run function {datapack_name}:{function_name}'
    ]

def create_pack_meta(minecraft_version='1.6.1', description=None, author=None):
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


def import_from_file(path, extension='mcfunction'):
    '''
    This functions help with importing files instead of writing them.
    The files has to exist on the user's computer to be imported.

    :param path:        The path where the resource has to be find.
    :param extension:   The extension of the resource [e.g. ".mcfunction", ".json", ".dat"].
    :return:            None or OS-Error if the resource can not be found or read.
    '''
    try:
        with open(f'{path}.{extension}', 'r') as f:
            r = [line.replace('\n', '') for line in f if line not in ['', ' ', '\n']]
            f.close()
        return r
    except:
        raise ValueError(f'Could not read the file {path}.{extension}')


assert Datapack('TeSt tItLe').title == 'test title'