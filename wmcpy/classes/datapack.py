from os import mkdir
from shutil import rmtree
from .workspace import Workspace
from json import dump

class Datapack():
    def __init__(self, name, description, version):
        self.name = name
        self.description = description
        self.version = version
        self.workspaces = []
    def add_workspace(self, workspace: Workspace):
        self.workspaces.append(workspace)
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
                    if file != None:
                        mkdir(path + '/' + self.name + '/data/' + workspace.name + '/functions')
                        commands = ''
                        for command in file.commands:
                            commands += str(command) + '\n'
                        open(path + '/' + self.name + '/data/' + workspace.name + '/functions/' + file.name + '.mcfunction', 'w+', encoding='utf-8').write(commands)
            if workspace.raycasts != None:
                todo = ['/raycast', '/raycast/tags', '/raycast/tags/blocks', '/raycast/functions', '/raycast/functions/generated_raycast']
                for f in todo:
                    try:
                        mkdir(path + '/' + self.name + '/data' + f)
                    except:
                        pass
                try:
                    open(path + '/' + self.name + '/data/raycast/functions/load.mcfunction', 'w+').write('scoreboard objectives add ray_found dummy')
                except: pass
                for raycast_id in range(len(workspace.raycasts)):
                    raycast = workspace.raycasts[raycast_id]
                    try:
                        dump({"replace": False,"values": raycast.blocks}, open(path + '/' + self.name + '/data/raycast/tags/blocks/tohit_{}.json'.format(raycast_id), 'w+'))
                    except:
                        break
                    open(path + '/' + self.name + '/data/raycast/functions/generated_raycast/raycast_{}.mcfunction'.format(raycast_id), 'w+').write('execute store result score raycast_{0} ray_found run clone ~-15 ~-4 ~-15 ~15 ~15 ~15 ~-15 ~-4 ~-15 filtered air force'.format(raycast_id))