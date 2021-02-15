from shutil import rmtree
from time import time
import os
from .files import *

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

assert Datapack('TeSt tItLe').title == 'test title'
