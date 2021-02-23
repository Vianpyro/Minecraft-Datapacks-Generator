class Selector():
    def __init__(self, selector_type: str,**kwargs):
        if not selector_type.startswith('@'):
            self.selector_type = selector_type
        else:
            self.selector_type = selector_type[1:]
        self.args = kwargs
    def __str__(self) -> str:
        toreturn = '@' + self.selector_type + '['
        for element in self.args:
            toreturn += element + '=' + str(self.args[element]) + ', '
        return toreturn[:-2] + ']'
