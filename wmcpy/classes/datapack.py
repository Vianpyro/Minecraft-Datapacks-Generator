from os import mkdir
from shutil import Error, rmtree
from .workspace import Workspace
from .raycast import Raycast
from json import dump
from time import sleep

class Datapack():
    def __init__(self, name, description, version):
        self.name = name
        self.description = description
        self.version = version
        self.workspaces = []
        self.raycasts = None
    def add_workspace(self, workspace: Workspace):
        self.workspaces.append(workspace)
    def add_raycast(self, raycast: Raycast):
        if self.raycasts == None: self.raycasts = []
        self.raycasts.append(raycast)
    def build(self, path: str, force=False):
        try:
            mkdir(path + '/' + self.name)
        except FileExistsError:
            if force:
                rmtree(path + '/' + self.name)
                mkdir(path + '/' + self.name)
            else:
                raise FileExistsError('dir early exist with this path, add force=True to the function to ignore this error and to delete the dir to re-create it')
        dump({"pack": { "pack_format": int(self.version),"description": self.description}}, open(path + '/' + self.name + '/pack.mcmeta', 'w+', encoding='utf-8'))
        mkdir(path + '/' + self.name + '/data')
        for workspace in self.workspaces:
            mkdir(path + '/' + self.name + '/data/' + workspace.name)
            if workspace.files != None:
                for file in workspace.files:
                    print('ok')
                    if file != None:
                        print('ok')
                        mkdir(path + '/' + self.name + '/data/' + workspace.name + '/functions')
                        commands = ''
                        for command in file.commands:
                            commands += str(command) + '\n'
                        open(path + '/' + self.name + '/data/' + workspace.name + '/functions/' + file.name + '.mcfunction', 'w+', encoding='utf-8').write(commands)
        if self.raycasts != None:
            todo = ['/raycast', '/raycast/tags', '/raycast/tags/blocks', '/raycast/functions', '/raycast/functions/generated_raycast']
            for f in todo:
                try:
                    mkdir(path + '/' + self.name + '/data' + f)
                except:
                    pass
            try:
                open(path + '/' + self.name + '/data/raycast/functions/load.mcfunction', 'w+').write('scoreboard objectives add ray_found dummy')
            except: pass
            for raycast_id in range(len(self.raycasts)):
                raycast = self.raycasts[raycast_id]
                t = (raycast.range[0] * 2) * (raycast.range[1] * 2)
                print(t)
                if t * (raycast.range[2] * 2) >= 32768: raise Error('The maximum block cloning limit is set to 32767')
                del t
                dump({"replace": False,"values": raycast.blocks}, open(path + '/' + self.name + '/data/raycast/tags/blocks/tohit_{}.json'.format(raycast_id), 'w+'))
                open(path + '/' + self.name + '/data/raycast/functions/generated_raycast/raycast_{}.mcfunction'.format(raycast_id), 'w+').write('execute store result score raycast_{3} ray_found run clone ~-{0} ~-{1} ~-{2} ~{0} ~{1} ~{2} ~-{0} ~-{1} ~-{2} filtered {4} force'.format(raycast.range[0], raycast.range[1], raycast.range[2], raycast_id, '#raycast:tohit_' + str(raycast_id)))