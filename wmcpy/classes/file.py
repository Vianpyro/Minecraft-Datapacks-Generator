class File():
    def __init__(self, name):
        self.name = name
        self.commands = None
    def set_content(self, commands: list):
        self.commands = commands
