from .file import File
from .predicate import Predicate
from .custom import Custom

class Workspace():
    def __init__(self, name: str) -> None:
        if name.endswith('.mcfunction'): name.replace('.mcfunction', '', 1)
        self.name = name
        self.files = None
        self.raycasts = None
        self.predicates = None
        self.customs = None
    def add_file(self, file: File):
        if self.files == None: self.files = [file]
        else: self.files.append(file)
    def add_predicate(self, predicate: Predicate):
        if self.predicates == None: self.predicates = [predicate]
        else: self.predicates.append(predicate)
    def add_custom(self, custom: Custom):
        if self.customs == None: self.customs = []
        self.customs.append(custom)
