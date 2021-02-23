class Raycast():
    def __init__(self, blocks: list = ['stone'], range: tuple = (15, 15, 15), type: str='b', docmd: str='say hi') -> None:
        """
        range: tuple = (x, y, z)
        """
        self.blocks = blocks
        self.range = range
        self.type = type
        self.docmd = docmd