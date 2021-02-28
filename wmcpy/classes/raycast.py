class Raycast():
    def __init__(self, blocks: list = ['stone'], range: tuple = (15, 15, 15), type: str='b', docmd: str='say hi') -> None:
        """
        range: tuple = (x, y, z)
        """
        self.blocks = blocks
        self.range = range
        self.type = type
        self.docmd = docmd
    """def __str__(self) -> str:
        toret = ''
        if self.type == 'b':
            for x in range(int('-' + str(self.range[0])), self.range[0]):
                for y in range(int('-' + str(self.range[1])) ,self.range[1]):
                    for z in range(int('-' + str(self.range[2])) ,self.range[2]):
                        toret += 'execute if block ~{} ~{} ~{} {} run '.format(x, y, z, self.block) + self.docmd + '\n'
            return toret"""