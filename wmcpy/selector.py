class Selector:
    def __init__(self, target_entity:str='@s',
                 advancements:str=None,
                 distance:str=None, dx:str=None, dy:str=None, dz:str=None,
                 entity_type:str=None,
                 gamemode:str=None, level:str=None, limit:str=None,
                 name:str=None, nbt:str=None,
                 scores:str=None, sort:str=None,
                 tag:str=None, team:str=None,
                 x:str=None, x_rotation:str=None,
                 y:str=None, y_rotation:str=None,
                 z:str=None
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

    def __str__(self) -> str:
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