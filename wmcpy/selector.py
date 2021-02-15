class Selector:
    def __init__(self, target_entity='@s',
                 advancements=None,
                 distance=None, dx=None, dy=None, dz=None,
                 entity_type=None,
                 gamemode=None, level=None, limit=None,
                 name=None, nbt=None,
                 scores=None, sort=None,
                 tag=None, team=None,
                 x=None, x_rotation=None,
                 y=None, y_rotation=None,
                 z=None
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

    def __str__(self):
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