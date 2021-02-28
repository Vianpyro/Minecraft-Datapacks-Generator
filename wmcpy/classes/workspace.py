from .file import File

class Workspace():
    def __init__(self, name: str) -> None:
        if name.endswith('.mcfunction'): name.replace('.mcfunction', '', 1)
        self.name = name
        self.files = None
        self.raycasts = None
    def add_file(self, file: File):
        if self.files == None: self.files = []
        self.files.append(file)